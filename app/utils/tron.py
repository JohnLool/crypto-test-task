from tronpy import AsyncTron
from tronpy.exceptions import AddressNotFound
from .logger import logger


async def get_wallet_info(address: str) -> dict:
    async with AsyncTron(network="mainnet") as client:
        try:
            bandwidth = await client.get_bandwidth(address)
            balance = await client.get_account_balance(address)
            energy = await client.get_energy(address)
        except AddressNotFound:
            logger.error(f"Tron address {address} not found")
            raise ValueError("Invalid Tron address")

        return {
            "trx_balance": balance,
            "bandwidth": bandwidth,
            "energy": energy,
        }
