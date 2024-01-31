import re
from typing import Any, Callable, Dict, Iterable, Tuple, Union

try:
    import regex
    AnyPattern = Union[regex.Pattern, re.Pattern]
    AnyMatch = Union[regex.Match, re.Match]
except ModuleNotFoundError:
    AnyPattern = Union[re.Pattern]
    AnyMatch = Union[re.Match]

StrOrBytes = Union[str, bytes]
CanTransformToPattern = Union[AnyPattern, StrOrBytes]
TextParser = Callable[[str], Dict[str, Any]]
PatternOrParser = Union[
    TextParser,
    AnyPattern
]
AcceptableAsInputPattern = Tuple[CanTransformToPattern, Iterable[str]]
AcceptableAsInputParser = Tuple[TextParser, Iterable[str]]
AcceptableAsInputPatternOrParser = Tuple[
    Union[
        TextParser,
        CanTransformToPattern
    ],
    Iterable[str]
]

__all__ = [
        "AnyPattern",
        "AnyMatch",
        "StrOrBytes",
        "CanTransformToPattern",
        "TextParser",
        "PatternOrParser",
        "AcceptableAsInputPattern",
        "AcceptableAsInputParser",
        "AcceptableAsInputPatternOrParser"
]
