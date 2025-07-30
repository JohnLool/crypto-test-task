from __future__ import annotations
from datetime import datetime
from decimal import Decimal
from typing import Any

from pydantic import BaseModel, Field, ConfigDict, field_validator


class WalletLog(BaseModel):
    id: int
    wallet_address: str = Field(..., max_length=64)
    trx_balance: Decimal = Field(...)
    bandwidth: int
    energy: int
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

    @field_validator("trx_balance", mode="before")  # noqa
    @classmethod
    def ensure_decimal(cls, v: Any):
        if isinstance(v, float) or isinstance(v, str):
            return Decimal(str(v))
        return v
