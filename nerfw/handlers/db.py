from sqlalchemy.orm import Session

from nerfw.database import SessionLocal


class DbHandler:
    """Database handler"""

    def __init__(self):
        self.db = None

    async def __aenter__(self) -> Session:
        """
        Get a database session.

        :return: Database session
        """

        self.db = SessionLocal()
        return self.db

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        """
        Close the database session.

        :param exc_type: Type of exception
        :param exc_val: Exception value
        :param exc_tb: Exception traceback
        :return: None
        """

        self.db.close()
        self.db = None

    async def get_db(self) -> Session:
        """
        Get a database session.

        :return: Database session
        """

        try:
            self.db = SessionLocal()
            yield self.db
        finally:
            self.db.close()
            self.db = None
