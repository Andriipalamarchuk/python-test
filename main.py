from fastapi import FastAPI
from dotenv import dotenv_values

from api.url_route import router as url_router
from database.database_client import check_if_index_exists

app = FastAPI()
app.include_router(url_router, tags=["url"], prefix="/url")
check_if_index_exists()