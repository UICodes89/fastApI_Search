from fastapi import Depends, FastAPI


from .dependencies import get_query_token, get_token_header
from .internal import admin
from .routers import search

app = FastAPI(dependencies=[Depends(get_query_token)])



app.include_router(search.router)
app.include_router(
    admin.router,
    prefix="/admin",
    tags=["admin"],
    dependencies=[Depends(get_token_header)],
    responses={418: {"description": "I'm a teapot"}},
)


