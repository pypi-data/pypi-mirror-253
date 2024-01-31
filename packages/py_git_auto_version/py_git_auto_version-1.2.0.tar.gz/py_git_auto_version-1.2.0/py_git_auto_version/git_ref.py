from pathlib import PurePosixPath
from typing import ClassVar, Optional, Tuple
import warnings

from more_itertools import sort_together
from py_git_auto_version.extractors.abc.version_extractor_base import VersionInformationExtractor
from py_git_auto_version.git import Git

old_print = print
try:
    import rich
    import rich.pretty

    rich.pretty.install()
    print = rich.pretty.pprint
except ModuleNotFoundError:
    print = old_print


class GitRef:
    _tag_path: ClassVar[PurePosixPath] = PurePosixPath("refs") / 'tags'
    _local_branch_base_path: ClassVar[PurePosixPath] = PurePosixPath("refs") / 'heads'
    _remote_branch_base_path: ClassVar[PurePosixPath] = PurePosixPath("refs") / 'remotes' / 'origin'

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        return (
            str(
                {
                    "hash": str(self.object_git_hash),
                    "full_branch_name": str(self.full_local_branch_name),
                    "remote_name": str(self.full_remote_branch_name),
                    "tag": str(self.tag_name),
                    "verbose": str(self.verbose)
                }
            )
        )

    def __rich_repr__(self):
        yield (
            "hash",
            None if self.object_git_hash is None else str(self.object_git_hash)
        )
        yield (
            "remote",
            None if self.full_remote_branch_name is None else str(self.full_remote_branch_name)
        )
        yield (
            "branch",
            None if self.full_local_branch_name is None else str(self.full_local_branch_name)
        )
        yield "tag", None if self.tag_name is None else str(self.tag_name)
        yield "verbose", self.verbose

    def _determine_tag(self, extractor: VersionInformationExtractor):
        if extractor is None:
            raise ValueError("given extractor is None")
        errlvl, points_at = Git.Tag.points_at(self.object_git_hash, return_errorcode=True)
        if len(points_at.strip()) > 0:
            use_tag = points_at.split("\n")
        else:
            errlvl, merged = Git.Tag.merged(self.object_git_hash, return_errorcode=True)
            use_tag = merged.split("\n")
        parsed_versions = []
        parsed_tags = []
        parsing_failed_tags = []
        for tag in use_tag:
            tag_info = extractor.extract_info(tag=tag)
            parsed_versions.append((int(tag_info['major']), (tag_info['minor']), (tag_info['micro'])))
            parsed_tags.append(tag)
        if len(parsing_failed_tags) > 0:
            if len(parsed_versions) == 0:
                raise ValueError(f"All tags failed to parse: {parsing_failed_tags}")
            else:
                warnings.warn(f"The following tags failed to parse: {parsing_failed_tags}")
        sorted_versions, sorted_tags = sort_together([parsed_versions, parsed_tags])
        max_version_tag: str = sorted_versions[-1]
        self.tag_name = self.__class__._tag_path / f"{max_version_tag}"

    def _determine_branch(self):
        errlvl, points_at = Git.Branch.points_at(self.object_git_hash, return_errorcode=True)

        def clean_branch_response(text: str):
            lines = text.split("\n")
            kept = []
            for line in lines:
                if line.startswith("* (HEAD detached"):
                    ...
                elif line.startswith("* "):
                    starred_branch = line[2:].strip()
                    kept.append(starred_branch)
                else:
                    kept.append(line.strip())
            return kept

        if len(points_at.strip()) > 0:
            use_branch = points_at
            kept_branch = clean_branch_response(use_branch)
        else:
            errlvl, use_branch = Git.Branch.contains(self.object_git_hash, return_errorcode=True)
            # if errlvl:
            #     print(use_branch, file=sys.stderr)
            kept_branch = clean_branch_response(use_branch)
        if len(kept_branch) == 0:
            # print(self)
            kept_branch.append("main")  # if there are not any branches, this was probably a tag ref
            # raise ValueError(
            #         "Cannot determine branch, probably a dangling commit"
            # )
        # rich.print(kept_branch)
        if "main" in kept_branch:
            self.full_remote_branch_name = self.__class__._remote_branch_base_path / "main"
            self.full_local_branch_name = self.__class__._local_branch_base_path / "main"
        elif len(kept_branch) == 1:
            bn = list(kept_branch)[0]
            self.full_remote_branch_name = self.__class__._remote_branch_base_path / bn
            self.full_local_branch_name = self.__class__._local_branch_base_path / bn
        elif len(kept_branch) > 1:
            raise ValueError(f"what do?: {kept_branch}")

    def __init__(
            self,
            ref_info: Tuple[str, str],
            extractor: VersionInformationExtractor,
            verbose=True
    ):
        self.verbose: bool = verbose
        self.object_git_hash: Optional[str] = None
        self.object_ref_type: Optional[str] = ref_info[1]
        self.tag_name: Optional[PurePosixPath] = None
        self.full_local_branch_name: Optional[PurePosixPath] = None
        self.full_remote_branch_name: Optional[PurePosixPath] = None
        if extractor is None:
            raise ValueError("Expected Extractor Object. Received None.")
        self.extractor: VersionInformationExtractor = extractor
        simple_ref_name = PurePosixPath(ref_info[0]).name
        if self.object_ref_type == "tag":
            full_ref = self.__class__._tag_path / simple_ref_name
            errlvl, self.object_git_hash = Git.RevParse.object(str(full_ref), return_errorcode=True)
            errlvl, points_at_output = Git.Tag.points_at(
                self.object_git_hash,
                return_errorcode=True
            )
            self.tag_name = (
                    self.__class__._tag_path / points_at_output
            )
            self._determine_branch()
        elif self.object_ref_type == "branch":
            full_ref = self.__class__._local_branch_base_path / simple_ref_name
            errlvl, self.object_git_hash = Git.RevParse.object(str(full_ref), return_errorcode=True)
            errlvl, points_at_output = Git.Branch.points_at(
                self.object_git_hash,
                include_remotes=False,
                include_local=True,
                return_errorcode=True
            )
            self.full_local_branch_name = (
                    self.__class__._local_branch_base_path /
                    points_at_output[2:]
            )
            self.full_remote_branch_name = (
                    self.__class__._remote_branch_base_path /
                    self.full_local_branch_name.name
            )
            self._determine_tag(extractor=extractor)
        elif self.object_ref_type == 'remote':
            full_ref = self.__class__._remote_branch_base_path / simple_ref_name
            errlvl, self.object_git_hash = Git.RevParse.object(str(full_ref), return_errorcode=True)
            errlvl, points_at_output = Git.Branch.points_at(
                self.object_git_hash,
                include_remotes=True,
                include_local=False,
                return_errorcode=True
            )
            self.full_remote_branch_name = (
                    self.__class__._remote_branch_base_path /
                    PurePosixPath(points_at_output[2:]).name
            )
            self.full_local_branch_name = (
                    self.__class__._local_branch_base_path /
                    self.full_remote_branch_name.name
            )
            self._determine_tag(
                extractor=extractor
            )
        else:
            raise RuntimeError(
                "unknown ref type: ", self.object_ref_type, "for ref:", self.object_git_hash
            )
