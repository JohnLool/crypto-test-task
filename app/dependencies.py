from app.core.database import get_session
from app.repositories.wallet_log_repo import WalletLogRepository
from app.services.wallet_log_service import WalletLogService

from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import Depends


async def get_wallet_log_repo(
    session: AsyncSession = Depends(get_session),
) -> WalletLogRepository:
    return WalletLogRepository(session)


async def get_wallet_log_service(
    repo: WalletLogRepository = Depends(get_wallet_log_repo),
) -> WalletLogService:
    return WalletLogService(repo)
