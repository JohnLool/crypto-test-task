from datetime import datetime
from decimal import Decimal
from typing import Any

from pydantic import BaseModel, Field, ConfigDict, field_validator


class WalletAddressRequest(BaseModel):
    wallet_address: str = Field(..., max_length=64)


class WalletLog(WalletAddressRequest):
    id: int
    trx_balance: Decimal = Field(...)
    bandwidth: int
    energy: int
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

    @field_validator("trx_balance", mode="before")  # noqa
    @classmethod
    def ensure_decimal(cls, v: Any) -> Decimal:
        if not isinstance(v, Decimal):
            return Decimal(str(v))
        return v
