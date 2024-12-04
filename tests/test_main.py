import asyncio
from httpx import AsyncClient
from main import app

async def test_read_main():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/tickets")
    assert response.status_code == 200
