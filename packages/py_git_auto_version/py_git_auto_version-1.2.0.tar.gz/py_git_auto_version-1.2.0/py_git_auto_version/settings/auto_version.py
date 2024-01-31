from typing import Any, AnyStr, Optional, Union

from py_git_auto_version.re_compile_func import re_compile_func
from pydantic import BaseSettings, validator
import regex


class PyGitAutoVersionSettings(BaseSettings):
    TAG_TO_VERSION_PATTERN: Optional[regex.Pattern[AnyStr]]
    USE_PACKAGING_PARSER_FOR_TAG: Optional[bool]
    DESCRIBE_LONG_PATTERN: Optional[regex.Pattern[AnyStr]]

    @classmethod
    def generate_defaults(cls):
        tag_to_version_pattern = re_compile_func(
            "^v?(?P<major>[0-9]+)[.](?P<minor>[0-9]+)[.](?P<patch>[0-9]+)$"
        )
        dl_pattern = re_compile_func(
            r"^(?P<tag_name>.+)[-](?P<commit_count>[0-9]+)[-](?P<short_hash>[0-9a-z]+)$"
        )
        return cls(
            TAG_TO_VERSION_PATTERN=tag_to_version_pattern,
            DESCRIBE_LONG_PATTERN=dl_pattern,
            USE_PACKAGING_PARSER_FOR_TAG=False
        )

    @classmethod
    def create_object_from_env(
            cls,
            _env_file: Optional[str] = None,
            _env_file_encoding: Optional[str] = None,
            fall_back_to_defaults_on_error=True
    ):
        try:
            result = cls(
                _env_file=_env_file,
                _env_file_encoding=_env_file_encoding
            )
            return result
        except ValueError as e:
            if not fall_back_to_defaults_on_error:
                raise e
        except TypeError as e:
            if not fall_back_to_defaults_on_error:
                raise e
        return cls.generate_defaults()

    @classmethod
    def generate_failover_try_env_then_dotenv_then_defaults(
            cls
    ):
        try:
            result = cls.create_object_from_env(
                fall_back_to_defaults_on_error=False
            )
            return result
        except ValueError:
            ...
        except TypeError:
            ...
        return cls.create_object_from_env(
            _env_file=".env",
            fall_back_to_defaults_on_error=True
        )

    @validator("TAG_TO_VERSION_PATTERN")
    def tvp_must_capture_version_segments_by_name(
            cls,
            v: regex.Pattern[AnyStr]
    ):
        if v is None:
            return v
        if isinstance(v, Union[str, bytes]):
            return re_compile_func(v)

    @validator("DESCRIBE_LONG_PATTERN")
    def dlp_must_capture_version_segments_by_name(
            cls,
            v: regex.Pattern[AnyStr]
    ):
        if v is None:
            return v
        if isinstance(v, Union[str, bytes]):
            return re_compile_func(v)

    class Config:
        env_prefix = "PY_GIT_AUTO_VERSION_"
        case_sensitive = True

        @validator("")
        def parse_env_var(cls, field_name: str, raw_val: str) -> Any:
            if field_name == 'TAG_TO_VERSION_PATTERN':
                return regex.compile(raw_val, flags=regex.V1)
            else:
                return cls.json_loads(raw_val)


__all__ = [
    PyGitAutoVersionSettings
]
