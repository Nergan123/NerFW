from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from nerfw.database import Base


class UserModel(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    password = Column(String)

    saves = relationship("SaveModel", back_populates="user")
