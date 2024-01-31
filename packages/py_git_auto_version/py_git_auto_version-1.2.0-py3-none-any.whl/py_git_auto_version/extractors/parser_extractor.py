from typing import Any, Dict, Iterable, List, Optional, Tuple

from py_git_auto_version.extractors.abc.version_extractor_base import VersionInformationExtractor
from py_git_auto_version.typing import AcceptableAsInputParser, TextParser


class ParserVersionInformationExtractor(VersionInformationExtractor[TextParser, str]):
    def __init__(
            self,
            tag_parser: AcceptableAsInputParser,
            additional_helper_parsers: Optional[
                Iterable[Tuple[str, AcceptableAsInputParser]]
            ] = None
    ):

        local_tag_parser: TextParser = tag_parser[0]
        local_tag_parser_include_item_keys: List[str] = list(tag_parser[1])
        if additional_helper_parsers is not None:
            local_helper_parsers: Dict[str, TextParser] = dict()
            local_helper_parsers_include_item_keys: Dict[str, List[str]] = dict()
            for name, input_tup in additional_helper_parsers:
                helper_obj, items_to_include = input_tup
                local_helper_parsers[name] = helper_obj
                local_helper_parsers_include_item_keys[name] = list(items_to_include)
        else:
            local_helper_parsers = dict()
            local_helper_parsers_include_item_keys = dict()
        super().__init__(
            tag_actor=local_tag_parser,
            tag_actor_include_item_keys=local_tag_parser_include_item_keys,
            additional_helper_actors=local_helper_parsers,
            additional_helper_actors_include_item_keys=local_helper_parsers_include_item_keys
        )

    def extract_info(self, tag: str) -> Dict[str, str]:
        parse_out: Dict[str, Any] = self._tag_actor(tag)
        results: Dict[str, str] = dict()
        for keyval in self._tag_actor_include_item_keys:
            results[keyval] = str(parse_out[keyval])
        return results

    def extract_info_with_helper(self, helper_name: str, text: str) -> Dict[str, str]:
        use_actor: TextParser = self._helper_actors[helper_name]
        use_include_keys: List[str] = self._helper_actors_include_item_keys[helper_name]
        parse_out: Dict[str, Any] = use_actor(text)
        results: Dict[str, str] = dict()
        for keyval in use_include_keys:
            results[keyval] = str(parse_out[keyval])
        return results

    def sub_with_helper(self, helper_name: str, repl: str, string: str) -> str:
        raise NotImplementedError("Parser is unable to assist with substitution")


__all__ = [
    "ParserVersionInformationExtractor"
]
