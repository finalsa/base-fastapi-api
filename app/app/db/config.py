from databases import Database
from sqlalchemy import create_engine, MetaData
from core.config import settings
from contextlib import closing

engine = None


db_url = "mysql://{}:{}@{}/{}".format(
    settings.sql_user,
    settings.sql_password,
    settings.sql_host,
    settings.sql_db
)


metadata = MetaData()
database = Database(db_url)


async def connect_db():
    global metadata
    global database
    global engine
    if(database.is_connected):
        return
    engine = create_engine(
        db_url
    )
    metadata.create_all(engine)
    await database.connect()


async def reset_db():
    global metadata
    global database
    global engine
    with closing(engine.connect()) as con:
        trans = con.begin()
        for table in reversed(metadata.sorted_tables):
            con.execute(table.delete())
        trans.commit()


async def disconnect_db():
    global database
    await database.disconnect()
