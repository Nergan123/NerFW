from sqladmin import ModelView

from nerfw.models import UserModel, SaveModel


class UserAdmin(ModelView, model=UserModel):
    column_list = [UserModel.id, UserModel.username, UserModel.role]


class SaveAdmin(ModelView, model=SaveModel):
    column_list = [SaveModel.id, SaveModel.name, SaveModel.user_id]
