from typing import Optional

from pydantic import BaseSettings


class GitHubActionEnvVars(BaseSettings):
    REF: Optional[str]
    REF_NAME: Optional[str]
    REF_TYPE: Optional[str]
    REPOSITORY: Optional[str]
    SHA: Optional[str]
    EVENT_NAME: Optional[str]
    BASE_REF: Optional[str]
    HEAD_REF: Optional[str]

    @classmethod
    def generate_failover_env_then_dotenv(cls):
        try:
            result = cls()
            return result
        except ValueError:
            ...
        except TypeError:
            ...
        return cls(_env_file=".env")

    class Config:
        env_prefix = "GITHUB_"
        case_sensitive = True


__all__ = [
    GitHubActionEnvVars
]
