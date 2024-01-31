import functools

from py_git_auto_version.typing import AcceptableAsInputPattern, AnyPattern
try:
    import regex as re_provider
    re_compile_func = functools.partial(re_provider.compile, flags=re_provider.V1)
except ModuleNotFoundError:
    import re as re_provider
    re_compile_func = re_provider.compile


def auto_prep_pattern_for_input(pattern_obj: AnyPattern):
    item_keys = []
    for grpname, grpind in pattern_obj.groupindex.items():
        item_keys.append(grpname)
    if len(item_keys) == 0:
        raise ValueError("Provided pattern does not specify any capture group names")
    return pattern_obj, tuple(item_keys)


def auto_compile_and_prep_pattern_for_input(pattern_str) -> AcceptableAsInputPattern:
    ptrn: AnyPattern = re_compile_func(pattern_str)
    return auto_prep_pattern_for_input(ptrn)


__all__ = [
    "re_compile_func",
    "re_provider",
    "auto_prep_pattern_for_input",
    "auto_compile_and_prep_pattern_for_input"
]
