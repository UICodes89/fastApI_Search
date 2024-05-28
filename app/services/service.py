import httpx

class HttpService:
    def __init__(self):
        self.client = httpx.AsyncClient()

    async def fetch_data(self, url: str):
        response = await self.client.get(url)
        response.raise_for_status()  # Raises an error if the request was unsuccessful
        return response.json()
    
    async def close(self):
        await self.client.aclose()
