from fastapi import APIRouter
from . import wallet

router = APIRouter(prefix="/api/v1")
router.include_router(wallet.router)
