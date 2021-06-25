from models import Session
from .utils import BaseCrud


class SessionCrud(BaseCrud):

    def __init__(self,) -> None:
        super().__init__(Session)


crud = SessionCrud()
