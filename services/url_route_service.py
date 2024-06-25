import datetime
from typing import Optional

from fastapi.encoders import jsonable_encoder
from database.database_client import get_database
from models.url import CreateUrlModel, UrlModel
from utils.url_shortener import shorten_url


class UrlRouteService:
    def create_minified_url(self, create_url_model: CreateUrlModel) -> UrlModel:
        create_url_data = jsonable_encoder(create_url_model)
        existing_url = self._check_if_url_already_minified(create_url_data["url"])
        if existing_url is not None:
            return existing_url
        
        original_url = create_url_data["url"]
        
        new_url = {
            "original_url": original_url,
            "minified_url": shorten_url(original_url),
            "created_at": datetime.datetime.now()
        }
        db = get_database()
        new_url = jsonable_encoder(new_url)
        insert_result = db["urls"].insert_one(new_url)

        return db["urls"].find_one({"_id": insert_result.inserted_id})

    def get_expanded_url(self, query: str) -> Optional[UrlModel]:
        db = get_database()

        return db["urls"].find_one({"minified_url": query})

    def _check_if_url_already_minified(self, url: str) -> Optional[UrlModel]:
        db = get_database()
        print(db)
        existing_minified_model = db["urls"].find_one({"original_url": url})
        if existing_minified_model is not None:
            return existing_minified_model
        
        return None