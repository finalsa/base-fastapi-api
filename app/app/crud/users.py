from models import User
from fastapi_helpers import BaseCrud


class UserCrud(BaseCrud):

    def __init__(self,) -> None:
        super().__init__(User)


crud = UserCrud()
