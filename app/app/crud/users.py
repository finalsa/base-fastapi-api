from models import User
from .utils import BaseCrud


class UserCrud(BaseCrud):

    def __init__(self,) -> None:
        super().__init__(User)


crud = UserCrud()
