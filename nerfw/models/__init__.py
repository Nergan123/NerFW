from nerfw.database import Base, engine
from user_model import UserModel  # noqa

Base.metadata.create_all(bind=engine)
