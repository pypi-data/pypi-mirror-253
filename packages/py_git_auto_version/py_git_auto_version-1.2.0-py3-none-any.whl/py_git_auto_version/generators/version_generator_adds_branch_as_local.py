from typing import Dict, List, Optional, Tuple, TypeVar

from py_git_auto_version.extractors.abc import VersionInformationExtractor
from py_git_auto_version.generators.abc.basic_version_generator import (
    BasicVersionGenerator
)
from py_git_auto_version.git_ref import GitRef
from py_git_auto_version.re_compile_func import re_compile_func
from py_git_auto_version.settings.auto_version import PyGitAutoVersionSettings
from py_git_auto_version.settings.github import GitHubActionEnvVars
from py_git_auto_version.typing import AcceptableAsInputPatternOrParser

A = TypeVar("A")


class VersionGeneratorAddsBranchAsLocal(BasicVersionGenerator[A]):
    def __init__(
            self,
            extractor: VersionInformationExtractor[A, str],
            auto_version_: Optional[PyGitAutoVersionSettings] = None,
            github_: Optional[GitHubActionEnvVars] = None,

    ):
        super().__init__(
            extractor=extractor,
            auto_version_=auto_version_,
            github_=github_
        )

    @staticmethod
    def get_default_helper_actors(
            auto_version_: PyGitAutoVersionSettings
    ) -> List[Tuple[str, AcceptableAsInputPatternOrParser]]:
        describe_long_pattern = re_compile_func(
            r"^(?P<tag_name>.+)[-](?P<commit_count>[0-9]+)[-](?P<short_hash>[0-9a-z]+)$"
        )
        describe_long_pattern_with_items: AcceptableAsInputPatternOrParser = (
            describe_long_pattern, ("tag_name", "commit_count", "short_hash")
        )
        branch_cleaner_step_1 = re_compile_func("[^0-9a-zA-Z.-]")
        branch_cleaner_step_2 = re_compile_func("[-]")
        branch_cleaner_step_3 = re_compile_func("^[.]*(?P<cleaned_text>.+)[.]*$")
        branch_cleaner_step_1_with_items: AcceptableAsInputPatternOrParser = (
            branch_cleaner_step_1, tuple([])
        )
        branch_cleaner_step_2_with_items: AcceptableAsInputPatternOrParser = (
            branch_cleaner_step_2, tuple([])
        )
        branch_cleaner_step_3_with_items: AcceptableAsInputPatternOrParser = (
            branch_cleaner_step_3, ("cleaned_text",)
        )

        return [
            ('describe_long', describe_long_pattern_with_items),
            ('clean_branch_1', branch_cleaner_step_1_with_items),
            ('clean_branch_2', branch_cleaner_step_2_with_items),
            ('clean_branch_3', branch_cleaner_step_3_with_items),
        ]

    def _get_extracts(
            self,
            source_refs: Dict[str, GitRef]
    ) -> Tuple[Dict[str, str], Dict[str, Dict[str, str]]]:
        tag_extracts, helper_extracts = super()._get_extracts(source_refs=source_refs)
        # get_version_from = source_refs['version_from']
        get_branch_from = source_refs['branch_from']
        branch_name = get_branch_from.full_remote_branch_name.name
        if branch_name != 'main':
            cleaned_branch_name = self._extractor.sub_with_helper(
                helper_name='clean_branch_1',
                repl="",
                string=branch_name
            )
            cleaned_branch_name = self._extractor.sub_with_helper(
                helper_name='clean_branch_2',
                repl=".",
                string=cleaned_branch_name
            )
            cleaned_branch_name = self._extractor.extract_info_with_helper(
                helper_name='clean_branch_3',
                text=cleaned_branch_name
            )['cleaned_text']
        else:
            cleaned_branch_name = 'main'
        helper_extracts['branch_name'] = {
            'cleaned_branch_name': cleaned_branch_name
        }
        return tag_extracts, helper_extracts

    def get_version(self) -> str:
        source_refs = self._get_source_refs()
        tag_extracts, helper_extracts = self._get_extracts(source_refs=source_refs)
        dl_extracts = helper_extracts['describe_long']
        extracted_tag = dl_extracts['tag_name']
        commit_count = dl_extracts['commit_count']
        tag_extracts = self._extractor.extract_info(extracted_tag)
        major_v = tag_extracts['major']
        minor_v = tag_extracts['minor']
        micro_v = tag_extracts['micro']
        version_text = f"{major_v}.{minor_v}.{micro_v}"
        cleaned_branch_name = helper_extracts['branch_name']['cleaned_branch_name']
        if cleaned_branch_name == 'main':
            if commit_count == '0':
                extra_version_text = ""
            else:
                extra_version_text = f".post{commit_count}"
        else:
            extra_version_text = f".dev{commit_count}+branch.{cleaned_branch_name}"
        return f"{version_text}{extra_version_text}"
