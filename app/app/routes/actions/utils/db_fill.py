from fastapi import Request, APIRouter
from utils import seeder
from db.config import reset_db

router = APIRouter()


@router.get("/db_fill/")
async def get_all(request: Request = {}):
    r = await seeder.db_fill()
    return {"status": r}


@router.get("/reset_db/")
async def reset_all(request: Request = {}):
    await reset_db()
    return {"status": "ok"}
