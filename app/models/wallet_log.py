from datetime import datetime
from decimal import Decimal
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, DateTime, Integer, Numeric, func
from app.core.database import Base


class WalletLogOrm(Base):
    __tablename__ = "wallet_logs"

    id: Mapped[int] = mapped_column(primary_key=True)
    wallet_address: Mapped[str] = mapped_column(String(64), nullable=False, index=True)
    trx_balance: Mapped[Decimal] = mapped_column(
        Numeric(precision=30, scale=8), nullable=False
    )
    bandwidth: Mapped[int] = mapped_column(Integer, nullable=False)
    energy: Mapped[int] = mapped_column(Integer, nullable=False)

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now()
    )
