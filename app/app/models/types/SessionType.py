from db import MainMeta
import ormar as orm


class SessionType(orm.Model):

    id: int = orm.Integer(name="price_type_id", primary_key=True)
    name: str = orm.String(max_length=20, unique=True)
    description: str = orm.String(max_length=100, server_default='')
    is_active: bool = orm.Boolean(default=False)
    for_platform: bool = orm.Boolean(default=False)

    async def load_data(self):
        return self

    class Meta(MainMeta):
        tablename = "session_types"
