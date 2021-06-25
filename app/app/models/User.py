from db import MainMeta
import ormar as orm
from .types import UserType


class User(orm.Model):
    id: int = orm.Integer(name="user_id", primary_key=True,)
    name: str = orm.String(max_length=100)
    user_name: str = orm.String(max_length=100, nullable=True, unique=True)
    phone: str = orm.String(max_length=20, default = "")
    email: str = orm.String(max_length=254, default = "")
    password: str = orm.Text(default = "")
    user_type: UserType = orm.ForeignKey(
        UserType, nullable = False, ondelete='CASCADE', onupdate='CASCADE'
    )

    class Meta(MainMeta):
        tablename = "users"

    async def load_data(self):
        return self
