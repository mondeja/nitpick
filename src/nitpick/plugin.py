"""Flake8 plugin to check files."""
import itertools
import logging
from pathlib import Path

import attr

from nitpick import __version__
from nitpick.config import NitpickConfig
from nitpick.constants import PROJECT_NAME
from nitpick.files.base import BaseFile
from nitpick.generic import get_subclasses
from nitpick.mixin import NitpickMixin
from nitpick.typedefs import YieldFlake8Error

LOGGER = logging.getLogger(__name__)


@attr.s(hash=False)
class NitpickChecker(NitpickMixin):
    """Main plugin class."""

    # Plugin config
    name = PROJECT_NAME
    version = __version__

    # NitpickMixin
    error_base_number = 100

    # Plugin arguments passed by Flake8
    tree = attr.ib(default=None)
    filename = attr.ib(default="(none)")

    def run(self) -> YieldFlake8Error:
        """Run the check plugin."""
        # An __init__() function is already provided by @attr.s
        self.config = NitpickConfig().get_singleton()  # pylint: disable=attribute-defined-outside-init

        if not self.config.find_root_dir(self.filename):
            yield self.flake8_error(1, "No root dir found (is this a Python project?)")
            return []

        if not self.config.find_main_python_file():
            yield self.flake8_error(2, "No Python file was found under the root dir {!r}".format(self.config.root_dir))
            return []

        current_python_file = Path(self.filename)
        if current_python_file.absolute() != self.config.main_python_file.absolute():
            # Only report warnings once, for the main Python file of this project.
            LOGGER.info("Ignoring file: %s", self.filename)
            return []
        LOGGER.info("Nitpicking file: %s", self.filename)

        yield from itertools.chain(self.config.merge_styles(), self.check_files(True), self.check_files(False))

        for checker_class in get_subclasses(BaseFile):
            checker = checker_class()
            yield from checker.check_exists()

        return []

    def check_files(self, present: bool) -> YieldFlake8Error:
        """Check files that should be present or absent."""
        # TODO: validate with schemas
        key = "present" if present else "absent"
        message = "exist" if present else "be deleted"
        absent = not present
        for file_name, extra_message in self.config.files.get(key, {}).items():
            file_path = self.config.root_dir / file_name  # type: Path
            exists = file_path.exists()
            if (present and exists) or (absent and not exists):
                continue

            full_message = "File {} should {}".format(file_name, message)
            if extra_message:
                full_message += ": {}".format(extra_message)

            yield self.flake8_error(3 if present else 4, full_message)