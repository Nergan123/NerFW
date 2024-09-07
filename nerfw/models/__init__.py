from nerfw.database import Base, engine
from nerfw.models.save_model import SaveModel  # noqa F401
from nerfw.models.user_model import UserModel  # noqa F401

Base.metadata.create_all(bind=engine)
