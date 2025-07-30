from typing import Sequence
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import select, desc
from app.models.wallet_log import WalletLogOrm
from app.repositories.abstract_repo import AbstractRepository
from app.logger import logger


class WalletLogRepository(AbstractRepository[WalletLogOrm]):
    def __init__(self, session: AsyncSession):
        self.session = session

    async def add(self, log_dict: dict) -> WalletLogOrm:
        log = WalletLogOrm(**log_dict)
        try:
            self.session.add(log)
            await self.session.commit()
            await self.session.refresh(log)
            return log
        except SQLAlchemyError as e:
            logger.error(f"Error creating wallet log: {e}")
            await self.session.rollback()
            raise

    async def get_list(
        self, *, offset: int = 0, limit: int = 100
    ) -> Sequence[WalletLogOrm]:
        stmt = (
            select(WalletLogOrm)
            .order_by(desc(WalletLogOrm.created_at))
            .offset(offset)
            .limit(limit)
        )
        result = await self.session.execute(stmt)
        return result.scalars().all()
