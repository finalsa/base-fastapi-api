import ormar as orm
from .config import metadata, database

class MainMeta(orm.ModelMeta):
    metadata = metadata
    database = database
