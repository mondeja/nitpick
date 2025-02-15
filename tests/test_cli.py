"""CLI tests."""
import pytest
import tomlkit

from nitpick.constants import DOT_NITPICK_TOML, PYPROJECT_TOML, READ_THE_DOCS_URL, TOOL_NITPICK_KEY
from nitpick.style import StyleManager
from nitpick.style.fetchers import Scheme
from tests.helpers import ProjectMock


def test_simple_error(tmp_path):
    """A simple error on the CLI."""
    project = (
        ProjectMock(tmp_path)
        .style(
            """
            ["pyproject.toml".tool.black]
            line-length = 100
            """
        )
        .pyproject_toml(
            """
            [tool.blabla]
            something = 22
            """
        )
    )

    project.cli_run(
        f"""
        {str(project.root_dir / "pyproject.toml")}:1: NIP318  has missing values:
        [tool.black]
        line-length = 100
        """
    )


@pytest.mark.parametrize("config_file", [DOT_NITPICK_TOML, PYPROJECT_TOML])
def test_config_file_already_has_tool_nitpick_section(tmp_path, config_file):
    """Test if both config files already exist."""
    project = ProjectMock(tmp_path, pyproject_toml=False, setup_py=True).save_file(
        config_file,
        f"""
        [{TOOL_NITPICK_KEY}]
        style = ['/this/should/not/be/validated-yet.toml']
        """,
    )
    project.cli_init(f"The config file {config_file} already has a [{TOOL_NITPICK_KEY}] section.", exit_code=1)


def test_create_basic_dot_nitpick_toml(tmp_path):
    """If no config file is found, create a basic .nitpick.toml."""
    project = ProjectMock(tmp_path, pyproject_toml=False, setup_py=True)
    url = StyleManager.get_default_style_url()
    project.cli_init(
        f"A [{TOOL_NITPICK_KEY}] section was created in the config file: {DOT_NITPICK_TOML}"
    ).assert_file_contents(
        DOT_NITPICK_TOML,
        f"""
        [{TOOL_NITPICK_KEY}]
        # Generated by the 'nitpick init' command
        # More info at {READ_THE_DOCS_URL}configuration.html
        style = ['{url}']
        """,
    )
    assert url.scheme == Scheme.PY


def test_init_empty_pyproject_toml(tmp_path):
    """If no config file is found, create a basic .nitpick.toml."""
    project = ProjectMock(tmp_path, pyproject_toml=False, setup_py=True)
    url = StyleManager.get_default_style_url()
    project.pyproject_toml("").cli_init(
        f"A [{TOOL_NITPICK_KEY}] section was created in the config file: {PYPROJECT_TOML}"
    ).assert_file_contents(
        PYPROJECT_TOML,
        f"""
        [{TOOL_NITPICK_KEY}]
        # Generated by the 'nitpick init' command
        # More info at {READ_THE_DOCS_URL}configuration.html
        style = ['{url}']

        """,
    )
    assert url.scheme == Scheme.PY


@pytest.mark.parametrize(
    "styles",
    [
        (),  # no arguments, default style
        ("https://github.com/andreoliwa/nitpick/blob/develop/initial.toml", "./local.toml"),
    ],
)
def test_add_tool_nitpick_section_to_pyproject_toml(tmp_path, styles):
    """Add a [tool.nitpick] section to pyproject.toml."""
    project = ProjectMock(tmp_path).pyproject_toml(
        """
        [tool.black]
        line-length = 120
        """
    )
    expected = styles or [StyleManager.get_default_style_url()]

    project.cli_init(
        f"A [{TOOL_NITPICK_KEY}] section was created in the config file: {PYPROJECT_TOML}", *styles
    ).assert_file_contents(
        PYPROJECT_TOML,
        f"""
        [tool.black]
        line-length = 120

        [{TOOL_NITPICK_KEY}]
        # Generated by the 'nitpick init' command
        # More info at {READ_THE_DOCS_URL}configuration.html
        style = {tomlkit.array([tomlkit.string(str(url)) for url in expected]).as_string()}
        """,
    )
