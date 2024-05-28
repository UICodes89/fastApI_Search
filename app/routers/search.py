import httpx 
from fastapi import APIRouter, Depends, HTTPException

from ..dependencies import get_token_header
from ..services.service import HttpService

router = APIRouter(
    prefix="/v1",
    tags=["items"],
    dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},
)


fake_items_db = {"plumbus": {"name": "Plumbus"}, "gun": {"name": "Portal Gun"}}

async def get_http_service():
    service = HttpService()
    try:
        yield service
    finally:
        await service.close()


@router.get("/search")
async def read_item(http_service: HttpService = Depends(get_http_service)):
    url = "https://bikeindex.org/api/v3/search"  # Replace with your desired URL
    try:
        data = await http_service.fetch_data(url)
        return data
    except httpx.HTTPStatusError as exc:
        raise HTTPException(status_code=exc.response.status_code, detail=str(exc))

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))