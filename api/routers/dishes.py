from typing import cast
from fastapi import APIRouter, status, HTTPException, Response

from api.routers.dish import DishResource
from data.model.dish import Dish
from service.dishes_service import DishesService

dishes_service : DishesService = DishesService()

router = APIRouter(
    prefix = "/dishes",
    tags = ["dishes"]
)


@router.get(
        path = "/",
        status_code = status.HTTP_200_OK,
        response_model = list[DishResource])
async def get() -> list[DishResource]:
    result: list[Dish] | None = dishes_service.get()
    return cast(list[DishResource], result)


@router.post(
    path = "/",
    status_code = status.HTTP_200_OK,
    response_model = DishResource
)
async def post(item: DishResource) -> DishResource: 
    result: Dish | None = dishes_service.add(cast(Dish, item))
    return cast(DishResource, result)


