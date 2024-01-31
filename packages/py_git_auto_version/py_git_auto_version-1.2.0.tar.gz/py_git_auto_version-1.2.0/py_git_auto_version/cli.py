import click
from py_git_auto_version.generators.abc.basic_version_generator import BasicVersionGenerator
from py_git_auto_version.generators.version_generator_adds_branch_as_local import VersionGeneratorAddsBranchAsLocal
from py_git_auto_version.settings.auto_version import PyGitAutoVersionSettings
from py_git_auto_version.settings.github import GitHubActionEnvVars


@click.command()
@click.option("--tag-pattern", type=str, default=None)
@click.option("--use-packaging-parser", is_flag=True)
@click.option("--append-branch/--no-append-branch", is_flag=True, default=None)
def main(tag_pattern, use_packaging_parser, append_branch):
    github_ = GitHubActionEnvVars.generate_failover_env_then_dotenv()
    if tag_pattern is None:  # or (append_branch is None):
        auto_version_ = PyGitAutoVersionSettings.generate_failover_try_env_then_dotenv_then_defaults()
        if tag_pattern is not None:
            auto_version_.TAG_TO_VERSION_PATTERN = tag_pattern
    else:
        auto_version_ = PyGitAutoVersionSettings(
                TAG_TO_VERSION_PATTERN=tag_pattern,
        )
    if append_branch:
        generator = VersionGeneratorAddsBranchAsLocal.create_with_defaults(auto_version_, github_=github_)
    else:
        generator = BasicVersionGenerator.create_with_defaults(auto_version_=auto_version_, github_=github_)
    print(generator.get_version())


if __name__ == "__main__":
    main()
