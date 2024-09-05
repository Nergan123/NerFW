import sys
from pathlib import Path

import nox

sys.path.insert(0, str(Path(__file__).parent))

from nerfw import __version__


@nox.session(python=None)
def lint(session: nox.Session):
    session.install("ruff")
    session.run("ruff", "check", ".")


@nox.session(python=None)
def towncrier(session: nox.Session):
    session.install("towncrier")
    version = __version__
    session.run("towncrier", "build", "--version", version, "--yes")
