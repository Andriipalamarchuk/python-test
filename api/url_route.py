from typing import Annotated
from fastapi import APIRouter, Body, HTTPException, status
from fastapi.params import Query

from models.url import CreateUrlModel, UrlModel
from services.url_route_service import UrlRouteService

router = APIRouter()

@router.post("/minify", response_description='Create a URL entry', status_code=status.HTTP_201_CREATED,response_model=UrlModel)
def create_minified_url(create_url_model: CreateUrlModel = Body(...)) -> UrlModel:
    route_service = UrlRouteService()
    url_model = route_service.create_minified_url(create_url_model)

    if url_model is None:
        # Should not never happen
        raise HTTPException(status_code=404, detail="Minified URL not found")
    
    return url_model

@router.get("/expand", response_description='Returns expanded url', status_code=status.HTTP_200_OK,response_model=UrlModel)
def get_expanded_url(q: Annotated[str | None, Query(max_length=100)] = None) -> UrlModel:
    if q is None:
        raise HTTPException(status_code=400, detail="Invalid query parameter")
    
    route_service = UrlRouteService()
    url_model = route_service.get_expanded_url(q)

    if url_model is None:
        raise HTTPException(status_code=404, detail="Minified URL not found")
    
    return url_model