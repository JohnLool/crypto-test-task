import pytest
from datetime import datetime
from decimal import Decimal
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.wallet_log import WalletLogOrm
from app.repositories.wallet_log_repo import WalletLogRepository


@pytest.mark.asyncio
async def test_add_wallet_log(async_session: AsyncSession):
    repo = WalletLogRepository(async_session)

    log_dict = {
        "wallet_address": "test_address",
        "trx_balance": Decimal("123.456"),
        "bandwidth": 300,
        "energy": 400,
    }

    result = await repo.add(log_dict)

    assert result.wallet_address == "test_address"
    assert result.trx_balance == Decimal("123.456")
    assert result.bandwidth == 300
    assert result.energy == 400
    assert isinstance(result.created_at, datetime)
    assert isinstance(result, WalletLogOrm)
