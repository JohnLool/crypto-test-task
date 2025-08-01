from app.repositories.wallet_log_repo import WalletLogRepository
from app.schemas.wallet_log import WalletLog
from app.utils.tron import get_wallet_info


class WalletLogService:
    def __init__(self, repo: WalletLogRepository):
        self.repo = repo

    async def create_wallet_log(self, address: str) -> WalletLog:
        wallet_data = await get_wallet_info(address)
        wallet_data["wallet_address"] = address
        wallet_log_orm = await self.repo.add(wallet_data)
        return WalletLog.model_validate(wallet_log_orm)

    async def get_logs(self, offset: int = 0, limit: int = 100) -> list[WalletLog]:
        wallet_logs_orm = await self.repo.get_list(offset=offset, limit=limit)
        return [WalletLog.model_validate(log) for log in wallet_logs_orm]
