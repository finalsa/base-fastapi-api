from models import Session
from fastapi_helpers import BaseCrud


class SessionCrud(BaseCrud):

    def __init__(self,) -> None:
        super().__init__(Session)


crud = SessionCrud()
