from solana.rpc.async_api import AsyncClient
from solana.publickey import PublicKey
from backend.database import get_subscriptions

import asyncio

async def monitor_contract(contract_address, callback):
    client = AsyncClient("https://api.mainnet-beta.solana.com")
    public_key = PublicKey(contract_address)
    print(f"Monitoring contract: {contract_address}")

    async for log in client.logs_subscribe(public_key):
        await callback(log.result)

async def start_monitoring():
    subscriptions = get_subscriptions()
    tasks = [monitor_contract(sub.contract_address, event_callback) for sub in subscriptions]
    await asyncio.gather(*tasks)

async def event_callback(log_data):
    print(f"Detected event: {log_data}")
    # Forward to AI or notification systems
