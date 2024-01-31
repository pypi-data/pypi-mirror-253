from abc import ABCMeta, abstractmethod
from typing import Dict, Generic, List, TypeVar

P = TypeVar("P")
K = TypeVar("K")


class VersionInformationExtractor(Generic[P, K], metaclass=ABCMeta):

    @abstractmethod
    def __init__(
            self,
            tag_actor: P,
            tag_actor_include_item_keys: List[K],
            additional_helper_actors: Dict[str, P],
            additional_helper_actors_include_item_keys: Dict[str, List[K]]
    ):
        self._tag_actor = tag_actor
        self._tag_actor_include_item_keys = tag_actor_include_item_keys
        self._helper_actors = additional_helper_actors
        self._helper_actors_include_item_keys = (
            additional_helper_actors_include_item_keys
        )

    @abstractmethod
    def extract_info(self, tag: str) -> Dict[str, str]:
        ...

    @abstractmethod
    def extract_info_with_helper(self, helper_name: str, text: str) -> Dict[str, str]:
        ...

    @abstractmethod
    def sub_with_helper(self, helper_name: str, repl: str, string: str) -> str:
        ...


__all__ = [
    "VersionInformationExtractor"
]
