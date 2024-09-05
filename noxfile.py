import nox


@nox.session(python=None)
def lint(session: nox.Session):
    session.install("ruff")
    session.run("ruff", "check", ".")


@nox.session(python=None)
def towncrier(session: nox.Session):
    session.install("towncrier")
    session.run("towncrier", "build", "--yes")
