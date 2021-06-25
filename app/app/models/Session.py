from db import MainMeta
from .User import User
import ormar as orm
from .types import SessionType
from datetime import datetime


class Session(orm.Model):

    id: int = orm.Integer(name="session_id", primary_key=True)
    ip: str = orm.String(max_length=100, nullable=False)
    token: str = orm.String(max_length=500, nullable=True, unique=True)
    session_type: SessionType = orm.ForeignKey(
        SessionType, nullable=False, ondelete='CASCADE', onupdate='CASCADE'
    )
    user: User = orm.ForeignKey(
        User, nullable=False, ondelete='CASCADE', onupdate='CASCADE'
    )
    creation_date = orm.DateTime(default=datetime.now(), nullable=False)
    expiration_date = orm.DateTime(default=datetime.now(), nullable=False)

    async def load_data(self):
        return self

    class Meta(MainMeta):
        tablename = "sessions"
