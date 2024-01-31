import subprocess
from typing import Iterable, Tuple, Union


class OnlyStatic:
    def __new__(cls, *args, **kwargs):
        raise RuntimeError('%s should not be instantiated' % cls)

    def __init__(self):
        raise RuntimeError('%s should not be instantiated' % self.__class__)


class CommandSubProcessGenerator:
    def __init__(self, base_command: Iterable[str]):
        self.base_command = tuple(base_command)

    def __call__(
            self,
            *args: Tuple[str, ...],
            return_errorcode=False
    ) -> Union[str, Tuple[int, str]]:
        command_string = " ".join(list(self.base_command) + list(args))
        # print(command_string)
        errorcode, output = subprocess.getstatusoutput(cmd=command_string)
        if return_errorcode:
            # print(output)
            return errorcode, output
        else:
            if errorcode:
                raise RuntimeError(
                        f"Git command returned an error code ({errorcode}). Output: '{output}'"
                )
            # print(output)
            return output


class Git(OnlyStatic):
    class RevParse(OnlyStatic):
        _base_command = CommandSubProcessGenerator(("git", "rev-parse"))

        @classmethod
        def _dispatch_command(
                cls,
                *args,
                symbolic=False,
                full_name=False,
                return_errorcode=False
        ):
            if symbolic:
                if full_name:
                    opts = ["--symbolic-full-name"]
                else:
                    opts = ["--symbolic"]
            else:
                opts = []
            return cls._base_command(
                    *(opts + list(args)),
                    return_errorcode=return_errorcode
            )

        @classmethod
        def object(
                cls,
                git_object,
                symbolic=False,
                full_name=False,
                return_errorcode=False
        ):
            return cls._dispatch_command(
                    git_object,
                    symbolic=symbolic,
                    full_name=full_name,
                    return_errorcode=return_errorcode
            )

        @classmethod
        def branches(
                cls,
                symbolic=False,
                full_name=False,
                return_errorcode=False
        ):
            return cls._dispatch_command(
                    "--branches",
                    symbolic=symbolic,
                    full_name=full_name,
                    return_errorcode=return_errorcode
            )

        @classmethod
        def tags(
                cls,
                symbolic=False,
                full_name=False,
                return_errorcode=False
        ):
            return cls._dispatch_command(
                    "--tags",
                    symbolic=symbolic,
                    full_name=full_name,
                    return_errorcode=return_errorcode
            )

        @classmethod
        def remotes(
                cls,
                symbolic=False,
                full_name=False,
                return_errorcode=False
        ):
            return cls._dispatch_command(
                    "--remotes",
                    symbolic=symbolic,
                    full_name=full_name,
                    return_errorcode=return_errorcode
            )

        @classmethod
        def all(
                cls,
                symbolic=False,
                full_name=False,
                return_errorcode=False
        ):
            return cls._dispatch_command(
                    "--all",
                    symbolic=symbolic,
                    full_name=full_name,
                    return_errorcode=return_errorcode
            )

    class Tag(OnlyStatic):
        _base_command = CommandSubProcessGenerator(("git", "tag"))

        @classmethod
        def _dispatch_command(
                cls,
                option_text,
                *args,
                negate_the_option=False,
                return_errorcode=False
        ):
            if negate_the_option:
                prefix = "--no-"
            else:
                prefix = "--"
            return cls._base_command(
                    *([f"{prefix}{option_text}"] + list(args)),
                    return_errorcode=return_errorcode
            )

        @classmethod
        def points_at(
                cls,
                git_object,
                negate_the_option=False,
                return_errorcode=False
        ):
            return cls._dispatch_command(
                    "points-at",
                    git_object,
                    negate_the_option=negate_the_option,
                    return_errorcode=return_errorcode
            )

        @classmethod
        def contains(
                cls,
                git_object,
                negate_the_option=False,
                return_errorcode=False
        ):
            return cls._dispatch_command(
                    "contains",
                    git_object,
                    negate_the_option=negate_the_option,
                    return_errorcode=return_errorcode
            )

        @classmethod
        def merged(
                cls,
                git_object,
                negate_the_option=False,
                return_errorcode=False
        ):
            return cls._dispatch_command(
                    "merged",
                    git_object,
                    negate_the_option=negate_the_option,
                    return_errorcode=return_errorcode
            )

    class Branch(OnlyStatic):
        _base_command = CommandSubProcessGenerator(("git", "branch"))

        @classmethod
        def _dispatch_command(
                cls,
                option_text,
                *args,
                negate_the_option=False,
                include_local=True,
                include_remotes=False,
                return_errorcode=False
        ):
            if include_local and include_remotes:
                filter_opt = "-a"
            elif include_local:
                filter_opt = ""
            elif include_remotes:
                filter_opt = "-r"
            else:
                raise ValueError("must include local or remotes (or both)")

            if negate_the_option:
                prefix = "--no-"
            else:
                prefix = "--"
            return cls._base_command(
                    *([f"{prefix}{option_text}"] + list(args) + [filter_opt]),
                    return_errorcode=return_errorcode
            )

        @classmethod
        def points_at(
                cls,
                git_object,
                negate_the_option=False,
                include_local=True,
                include_remotes=False,
                return_errorcode=False
        ):
            return cls._dispatch_command(
                    "points-at",
                    git_object,
                    negate_the_option=negate_the_option,
                    include_local=include_local,
                    include_remotes=include_remotes,
                    return_errorcode=return_errorcode
            )

        @classmethod
        def contains(
                cls,
                git_object,
                negate_the_option=False,
                include_local=True,
                include_remotes=False,
                return_errorcode=False
        ):
            return cls._dispatch_command(
                    "contains",
                    git_object,
                    negate_the_option=negate_the_option,
                    include_local=include_local,
                    include_remotes=include_remotes,
                    return_errorcode=return_errorcode
            )

        @classmethod
        def merged(
                cls,
                git_object,
                negate_the_option=False,
                include_local=True,
                include_remotes=False,
                return_errorcode=False
        ):
            return cls._dispatch_command(
                    "merged",
                    git_object,
                    negate_the_option=negate_the_option,
                    include_local=include_local,
                    include_remotes=include_remotes,
                    return_errorcode=return_errorcode
            )

        @classmethod
        def show_current(
                cls,
                return_errorcode=False
        ):
            return cls._dispatch_command(
                    option_text="show-current",
                    return_errorcode=return_errorcode
            )

    class Describe:
        _base_command = CommandSubProcessGenerator(("git", "describe"))

        @classmethod
        def _dispatch_command(
                cls,
                option_text: str,
                *args: Tuple[str, ...],
                return_errorcode=False
        ):
            return cls._base_command(
                    *([option_text] + list(args)),
                    return_errorcode=return_errorcode
            )

        @classmethod
        def long(
                cls,
                git_object,
                return_errorcode=False
        ):
            return cls._dispatch_command(
                    "--long",
                    git_object,
                    return_errorcode=return_errorcode
            )
