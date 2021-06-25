from fastapi import APIRouter
from .authorization import router as authorization_router

from . import utils

router = APIRouter()

router.include_router(utils.router)
router.include_router(authorization_router, tags=["authorization"])
