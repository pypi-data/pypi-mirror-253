from typing import Dict, Iterable, List, Optional, Tuple

from py_git_auto_version.extractors.abc.version_extractor_base import VersionInformationExtractor
from py_git_auto_version.re_compile_func import re_compile_func
from py_git_auto_version.typing import (
    AcceptableAsInputPattern,
    AnyMatch,
    AnyPattern,
    CanTransformToPattern,
    StrOrBytes
)


class PatternVersionInformationExtractor(VersionInformationExtractor[AnyPattern, str]):
    def __init__(
            self,
            tag_pattern: AcceptableAsInputPattern,
            additional_helper_patterns: Optional[
                Iterable[Tuple[str, AcceptableAsInputPattern]]
            ] = None
    ):
        def enforce_pattern_type(obj: CanTransformToPattern) -> AnyPattern:
            if isinstance(obj, AnyPattern):
                return obj
            elif isinstance(tag_pattern, StrOrBytes):
                return re_compile_func(obj)
            else:
                raise TypeError("pattern must be str,bytes, or a class that inherits from "
                                "re.Pattern or regex.Pattern")

        local_tag_pattern: AnyPattern = enforce_pattern_type(tag_pattern[0])
        local_tag_pattern_groupdict_keys: List[str] = list(tag_pattern[1])
        if additional_helper_patterns is not None:
            local_helper_patterns: Dict[str, AnyPattern] = dict()
            local_helper_patterns_groupdict_keys: Dict[str, List[str]] = dict()
            for name, input_tup in additional_helper_patterns:
                pattern_obj, items_to_include = input_tup
                local_helper_patterns[name] = enforce_pattern_type(pattern_obj)
                local_helper_patterns_groupdict_keys[name] = list(items_to_include)
        else:
            local_helper_patterns = dict()
            local_helper_patterns_groupdict_keys = dict()
        super().__init__(
            tag_actor=local_tag_pattern,
            tag_actor_include_item_keys=local_tag_pattern_groupdict_keys,
            additional_helper_actors=local_helper_patterns,
            additional_helper_actors_include_item_keys=local_helper_patterns_groupdict_keys
        )

    def extract_info(self, tag: str) -> Dict[str, str]:
        m: AnyMatch = self._tag_actor.match(tag)
        if not m:
            raise ValueError(f"could not pattern match: '{tag}' with pattern: {self._tag_actor}")
        cd: Dict[str, str] = m.groupdict()
        results = dict()
        for keyval in self._tag_actor_include_item_keys:
            results[keyval] = cd[keyval]
        return results

    def extract_info_with_helper(self, helper_name: str, text: str) -> Dict[str, str]:
        use_pattern = self._helper_actors[helper_name]
        use_include_keys = self._helper_actors_include_item_keys[helper_name]
        m: AnyMatch = use_pattern.match(text)
        if not m:
            raise ValueError(f"could not pattern match: '{text}' with pattern: {use_pattern}")
        cd: Dict[str, str] = m.groupdict()
        results = dict()
        for keyval in use_include_keys:
            results[keyval] = cd[keyval]
        return results

    def sub_with_helper(self, helper_name: str, repl: str, string: str) -> str:
        use_actor = self._helper_actors[helper_name]
        return use_actor.sub(repl=repl, string=string)


__all__ = [
    "PatternVersionInformationExtractor"
]
