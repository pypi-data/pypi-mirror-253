from typing import Dict, Iterable, List, Optional, Tuple

from py_git_auto_version.extractors.abc.version_extractor_base import VersionInformationExtractor
from py_git_auto_version.re_compile_func import re_compile_func
from py_git_auto_version.typing import (
    AcceptableAsInputPatternOrParser,
    AnyMatch,
    AnyPattern,
    CanTransformToPattern,
    PatternOrParser,
    StrOrBytes,
    TextParser
)


class MixedVersionInformationExtractor(VersionInformationExtractor[PatternOrParser, str]):
    def __init__(
            self,
            tag_handler: AcceptableAsInputPatternOrParser,
            additional_helper_handlers: Optional[
                Iterable[Tuple[str, AcceptableAsInputPatternOrParser]]
            ] = None
    ):
        def enforce_pattern_type(obj: CanTransformToPattern) -> AnyPattern:
            if isinstance(obj, AnyPattern):
                return obj
            elif isinstance(tag_handler, StrOrBytes):
                return re_compile_func(obj)
            else:
                raise TypeError("pattern must be str,bytes, or a class that inherits from "
                                "re.Pattern or regex.Pattern")

        local_tag_handler: PatternOrParser = enforce_pattern_type(tag_handler[0])
        local_tag_handler_include_item_keys: List[str] = list(tag_handler[1])
        if additional_helper_handlers is not None:
            local_helper_handlers: Dict[str, PatternOrParser] = dict()
            local_helper_handlers_include_item_keys: Dict[str, List[str]] = dict()
            for name, input_tup in additional_helper_handlers:
                helper_obj, items_to_include = input_tup
                local_helper_handlers[name] = enforce_pattern_type(helper_obj)
                local_helper_handlers_include_item_keys[name] = list(items_to_include)
        else:
            local_helper_handlers = dict()
            local_helper_handlers_include_item_keys = dict()
        super().__init__(
            tag_actor=local_tag_handler,
            tag_actor_include_item_keys=local_tag_handler_include_item_keys,
            additional_helper_actors=local_helper_handlers,
            additional_helper_actors_include_item_keys=local_helper_handlers_include_item_keys
        )
        # print('tag_actor', self._tag_actor)
        # print('tag_item_keys',self._tag_actor_include_item_keys)
        # print('helper_actor',self._helper_actors)
        # print('helper_item_keys',self._helper_actors_include_item_keys)

    def extract_info(self, tag: str) -> Dict[str, str]:
        results = dict()
        if isinstance(self._tag_actor, AnyPattern):
            m: AnyMatch = self._tag_actor.match(tag)
            if not m:
                raise ValueError(
                    f"could not pattern match: '{tag}' with pattern: {self._tag_actor}")
            output: Dict[str, str] = m.groupdict()
        elif isinstance(self._tag_actor, TextParser):
            output: Dict[str, str] = self._tag_actor(tag)
        else:
            raise RuntimeError(f"Behavior not defined for actor of type: {type(self._tag_actor)}")
        # print(self._tag_actor_include_item_keys)
        for keyval in self._tag_actor_include_item_keys:
            # print(keyval, type(keyval))
            results[keyval] = str(output[keyval])
        return results

    def extract_info_with_helper(self, helper_name: str, text: str) -> Dict[str, str]:
        results = dict()
        use_actor = self._helper_actors[helper_name]
        use_include_keys: List[str] = self._helper_actors_include_item_keys[helper_name]
        if isinstance(use_actor, AnyPattern):
            m: AnyMatch = use_actor.match(text)
            if not m:
                raise ValueError(f"could not pattern match: '{text}' with pattern: {use_actor}")
            output: Dict[str, str] = m.groupdict()

        elif isinstance(use_actor, TextParser):
            output: Dict[str, str] = use_actor(text)
        else:
            raise RuntimeError(f"Behavior not defined for actor of type: {type(use_actor)}")
        for keyval in use_include_keys:
            results[keyval] = str(output[keyval])
        return results

    def sub_with_helper(self, helper_name: str, repl: str, string: str) -> str:
        use_actor = self._helper_actors[helper_name]
        if not isinstance(use_actor, AnyPattern):
            raise NotImplementedError("Parser is unable to assist with substitution")
        return use_actor.sub(repl=repl, string=string)


__all__ = [
    "MixedVersionInformationExtractor"
]
