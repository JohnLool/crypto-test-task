from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, Query

from app.dependencies import get_wallet_log_service
from app.schemas.wallet_log import WalletLog, WalletAddressRequest
from app.services.wallet_log_service import WalletLogService

router = APIRouter(prefix="/wallet", tags=["wallet"])


@router.post("/", response_model=WalletLog, status_code=201)
async def create_wallet_log(
    body: WalletAddressRequest,
    service: WalletLogService = Depends(get_wallet_log_service),
):
    try:
        return await service.create_wallet_log(body.wallet_address)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/", response_model=list[WalletLog])
async def list_wallet_logs(
    offset: Annotated[int, Query(ge=0)] = 0,
    limit: Annotated[int, Query(ge=1, le=1000)] = 100,
    service: WalletLogService = Depends(get_wallet_log_service),
):
    return await service.get_logs(offset=offset, limit=limit)
