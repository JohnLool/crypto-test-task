import pytest
from httpx import AsyncClient
from decimal import Decimal


@pytest.mark.asyncio
async def test_create_wallet_log(monkeypatch, async_client: AsyncClient):
    async def mock_get_wallet_info(address: str) -> dict:
        return {
            "trx_balance": Decimal("999.99"),
            "bandwidth": 1000,
            "energy": 999,
        }

    monkeypatch.setattr("app.utils.tron.get_wallet_info", mock_get_wallet_info)

    payload = {"wallet_address": "test_address"}

    response = await async_client.post("/api/v1/wallet/", json=payload)

    assert response.status_code == 201
    data = response.json()
    print(data)

    assert data["wallet_address"] == payload["wallet_address"]
    assert Decimal(data["trx_balance"]) == Decimal("999.99")
    assert data["bandwidth"] == 1000
    assert data["energy"] == 999
