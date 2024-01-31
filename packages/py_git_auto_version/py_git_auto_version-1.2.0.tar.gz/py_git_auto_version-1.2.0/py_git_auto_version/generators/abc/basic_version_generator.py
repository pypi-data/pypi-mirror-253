from abc import ABCMeta
from enum import Enum
from typing import Any, Dict, Generic, Iterable, List, Optional, Tuple, TypeVar

from py_git_auto_version.extractors import MixedVersionInformationExtractor
from py_git_auto_version.extractors.abc import VersionInformationExtractor
from py_git_auto_version.git import Git
from py_git_auto_version.git_ref import GitRef
from py_git_auto_version.re_compile_func import (
    auto_compile_and_prep_pattern_for_input,
    auto_prep_pattern_for_input
)
from py_git_auto_version.settings.auto_version import PyGitAutoVersionSettings
from py_git_auto_version.settings.github import GitHubActionEnvVars
from py_git_auto_version.typing import AcceptableAsInputPatternOrParser


class VersioningScenario(Enum):
    GITHUB_ACTION_PUBLISH = 0  # "GithubPublish"
    GITHUB_ACTION_PULL_REQUEST = 1  # "GithubPullRequest"
    LOCAL_BUILD_BRANCH = 2  # "LocalBranch"
    LOCAL_BUILD_TAG = 3  # "LocalTag"


A = TypeVar("A")


class BasicVersionGenerator(Generic[A], metaclass=ABCMeta):
    def __init__(self, extractor: VersionInformationExtractor[A, str],
                 auto_version_: Optional[PyGitAutoVersionSettings] = None,
                 github_: Optional[GitHubActionEnvVars] = None,

                 ):
        self._extractor: VersionInformationExtractor[A, str] = extractor
        if auto_version_ is None:
            self._av_settings: PyGitAutoVersionSettings = PyGitAutoVersionSettings()
        else:
            self._av_settings: PyGitAutoVersionSettings = auto_version_
        if github_ is None:
            self._gh_settings: GitHubActionEnvVars = GitHubActionEnvVars()
        else:
            self._gh_settings: GitHubActionEnvVars = github_
        self._scenario = self._determine_scenario()
        self._gitrefs = dict()
        self._populate_required_gitrefs()

    def _determine_scenario(self) -> VersioningScenario:
        print("Determining scenario for versioning")

        def neither_none_nor_empty(val: Optional[str]) -> bool:
            return not ((val is None) or (len(val) == 0))

        if (neither_none_nor_empty(self._gh_settings.HEAD_REF) and neither_none_nor_empty(
                self._gh_settings.BASE_REF)):
            return VersioningScenario.GITHUB_ACTION_PULL_REQUEST
        elif neither_none_nor_empty(self._gh_settings.REF_NAME):
            return VersioningScenario.GITHUB_ACTION_PUBLISH
        else:
            tag_errlvl, tag_points_at_output = Git.Tag.points_at('HEAD', return_errorcode=True)
            branch_errlvl, branch_show_current_output = Git.Branch.show_current(
                return_errorcode=True)
            if tag_errlvl or branch_errlvl:
                errors_to_show = ["Git commands returned errors:"]
                if tag_errlvl:
                    errors_to_show.append(f"'git tag --points-at HEAD': '{tag_points_at_output}'\n")
                if branch_errlvl:
                    errors_to_show.append(
                        f"'git branch --show-current': '{branch_show_current_output}'")
                raise RuntimeError("\n".join(errors_to_show))
            tag_points_at_output = tag_points_at_output.strip()
            branch_show_current_output = branch_show_current_output.strip()
            branch_detached = len(branch_show_current_output) == 0
            head_is_not_tag = len(tag_points_at_output) == 0
            if head_is_not_tag and branch_detached:
                raise RuntimeError(
                    "HEAD does not point at a tag, and HEAD is detached, auto-versioning not "
                    "possible")
            if not branch_detached:
                # Even if HEAD is a tag, if we are not on main, we should follow any rules related
                # to naming the version based on the branch, that logic will be in the BUILD BRANCH
                # scenario
                return VersioningScenario.LOCAL_BUILD_BRANCH
            else:
                return VersioningScenario.LOCAL_BUILD_TAG

    def _populate_required_gitrefs(self):
        # defining sub-methods for better clarity
        def initialize_gh_action_pull_request_scenario():
            print("Initializing github action pull request scenario")
            base_ref_string = self._gh_settings.BASE_REF
            head_ref_string = self._gh_settings.HEAD_REF
            # print("base ref: ", base_ref_string)
            # print("head ref: ", head_ref_string)
            base_gitref = GitRef((base_ref_string, 'remote'),
                                 extractor=self._extractor)
            head_gitref = GitRef((head_ref_string, 'remote'),
                                 extractor=self._extractor)
            self._gitrefs["PR_HEAD_REF"] = head_gitref
            self._gitrefs["PR_BASE_REF"] = base_gitref

        def initialize_gh_action_publish_scenario():
            print("Initializing github action publish scenario")
            ref_name = self._gh_settings.REF_NAME
            ref_type = self._gh_settings.REF_TYPE
            # print((ref_name, ref_type))
            build_tag = GitRef((ref_name, ref_type),
                               extractor=self._extractor)
            if build_tag.object_ref_type != 'tag':
                raise ValueError("GithubAction ref must be provided as a "
                                 "GitRef object of type 'tag'")
            self._gitrefs["PUBLISH_REF"] = build_tag

        def initialize_local_tag_build_scenario():
            print("Initializing local tag build scenario")
            current_hash = Git.RevParse.object("HEAD")
            current_tag_name = Git.Tag.points_at(current_hash).strip()
            if len(current_tag_name.strip()) == 0:
                raise RuntimeError(f"Scenario is marked {self._scenario}, "
                                   "but HEAD does not have any tags pointing to it.")

            git_ref = GitRef((current_tag_name, 'tag'),
                             extractor=self._extractor)
            self._gitrefs["LOCAL_TAG_REF"] = git_ref

        def initialize_local_branch_build_scenario():
            print("Initializing local branch build scenario")
            current_branch_name = Git.Branch.show_current().strip()
            if len(current_branch_name) == 0:
                raise RuntimeError(
                    f"Scenario is marked: {self._scenario}, but could not get current branch")
            git_ref = GitRef((current_branch_name, 'branch'),
                             extractor=self._extractor)
            self._gitrefs["LOCAL_BRANCH_REF"] = git_ref

        # actual method code resumes here
        if self._scenario == VersioningScenario.GITHUB_ACTION_PULL_REQUEST:
            initialize_gh_action_pull_request_scenario()
        elif self._scenario == VersioningScenario.GITHUB_ACTION_PUBLISH:
            initialize_gh_action_publish_scenario()
        elif self._scenario == VersioningScenario.LOCAL_BUILD_TAG:
            initialize_local_tag_build_scenario()
        elif self._scenario == VersioningScenario.LOCAL_BUILD_BRANCH:
            initialize_local_branch_build_scenario()
        else:
            raise RuntimeError(f"Unknown Scenario: '{self._scenario}'")

    def __call__(self) -> str:
        return self.get_version()

    def _get_source_refs(self) -> Dict[str, GitRef]:
        def initialize_for_gh_action_pull_request() -> Dict[str, GitRef]:
            return {'branch_from': self._gitrefs['PR_BASE_REF'],
                    'version_from': self._gitrefs['PR_HEAD_REF']}

        def initialize_for_gh_action_publish() -> Dict[str, GitRef]:
            return {'branch_from': self._gitrefs['PUBLISH_REF'],
                    'version_from': self._gitrefs['PUBLISH_REF']}

        def initialize_for_local_branch_build() -> Dict[str, GitRef]:
            return {'branch_from': self._gitrefs['LOCAL_BRANCH_REF'],
                    'version_from': self._gitrefs['LOCAL_BRANCH_REF']}

        def initialize_for_local_tag_build() -> Dict[str, GitRef]:
            return {'branch_from': self._gitrefs['LOCAL_TAG_REF'],
                    'version_from': self._gitrefs['LOCAL_TAG_REF']}

        if self._scenario == VersioningScenario.GITHUB_ACTION_PULL_REQUEST:
            return initialize_for_gh_action_pull_request()
        elif self._scenario == VersioningScenario.GITHUB_ACTION_PUBLISH:
            return initialize_for_gh_action_publish()
        elif self._scenario == VersioningScenario.LOCAL_BUILD_TAG:
            return initialize_for_local_tag_build()
        elif self._scenario == VersioningScenario.LOCAL_BUILD_BRANCH:
            return initialize_for_local_branch_build()
        else:
            raise RuntimeError(f"Unknown Scenario: '{self._scenario}'")

    def _get_extracts(
            self,
            source_refs: Dict[str, GitRef]
    ) -> Tuple[Dict[str, str], Dict[str, Dict[str, str]]]:
        get_version_from = source_refs['version_from']
        # get_branch_from = source_refs['branch_from']
        # branch_name = get_branch_from.full_remote_branch_name.name
        describe_long_output = Git.Describe.long(get_version_from.object_git_hash)
        dl_extracts = self._extractor.extract_info_with_helper('describe_long',
                                                               describe_long_output)
        extracted_tag = dl_extracts['tag_name']
        # commit_count = dl_extracts['commit_count']
        tag_extracts = self._extractor.extract_info(extracted_tag)
        return tag_extracts, {
            'describe_long': dl_extracts
        }

    def get_version(self) -> str:
        source_refs = self._get_source_refs()
        tag_extracts, helper_extracts = self._get_extracts(source_refs=source_refs)
        major_v = tag_extracts['major']
        minor_v = tag_extracts['minor']
        micro_v = tag_extracts['micro']
        version_text = f"{major_v}.{minor_v}.{micro_v}"
        return version_text

    @staticmethod
    def get_default_tag_actor(
            auto_version_: PyGitAutoVersionSettings,
            use_packaging_parser: bool = False
    ) -> AcceptableAsInputPatternOrParser:
        if auto_version_.USE_PACKAGING_PARSER_FOR_TAG or use_packaging_parser:
            from packaging.version import parse as packaging_parse_version

            def parse_version(version: str) -> Dict[str, Any]:
                v = packaging_parse_version(version)
                return {x: getattr(v, x) for x in packaging_parsed_items}

            packaging_parsed_items: Iterable[str] = (
                'epoch', 'release', 'pre', 'post', 'dev', 'local', 'public', 'base_version', 'major',
                'minor', 'micro', 'is_prerelease', 'is_postrelease', 'is_devrelease'
            )
            return parse_version, packaging_parsed_items
        if auto_version_.TAG_TO_VERSION_PATTERN is not None:
            tag2version_pattern = auto_version_.TAG_TO_VERSION_PATTERN
            prepped_tag_pattern = auto_prep_pattern_for_input(tag2version_pattern)
        else:
            tag2version_pattern = (
                "^v?(?P<major>[0-9]+)[.](?P<minor>[0-9]+)[.](?P<micro>[0-9]+)$"
            )
            prepped_tag_pattern = auto_compile_and_prep_pattern_for_input(
                tag2version_pattern
            )
        return prepped_tag_pattern

    @staticmethod
    def get_default_helper_actors(
            auto_version_: PyGitAutoVersionSettings
    ) -> List[Tuple[str, AcceptableAsInputPatternOrParser]]:
        if auto_version_.DESCRIBE_LONG_PATTERN is not None:
            dl_pattern = auto_version_.DESCRIBE_LONG_PATTERN
            prepped_pattern = auto_prep_pattern_for_input(dl_pattern)
        else:
            dl_pattern = (
                r"^(?P<tag_name>.+)[-](?P<commit_count>[0-9]+)[-](?P<short_hash>[0-9a-z]+)$"
            )
            prepped_pattern = auto_compile_and_prep_pattern_for_input(dl_pattern)
        return [("describe_long", prepped_pattern)]

    @classmethod
    def get_default_extractor(
            cls,
            auto_version_: PyGitAutoVersionSettings
    ) -> VersionInformationExtractor:
        default_tag_handler = cls.get_default_tag_actor(auto_version_)
        default_helper_handlers = cls.get_default_helper_actors(auto_version_)
        return MixedVersionInformationExtractor(
            tag_handler=default_tag_handler,
            additional_helper_handlers=default_helper_handlers
        )

    @classmethod
    def create_with_defaults(
            cls,
            auto_version_: Optional[PyGitAutoVersionSettings],
            github_: Optional[GitHubActionEnvVars]
    ):
        extractor = cls.get_default_extractor(auto_version_)
        return cls(
            extractor=extractor,
            auto_version_=auto_version_,
            github_=github_
        )
