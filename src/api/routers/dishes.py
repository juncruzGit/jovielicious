from typing import cast
from fastapi import APIRouter, HTTPException, status

from src import Dish, DishResource
from ...dependencies import dishes_service_dep
from src import Routes


router = APIRouter(
    prefix = Routes.dishes,
    tags = ["dishes"]
)
@router.get(
        path = "",
        status_code = status.HTTP_200_OK,
        response_model = list[DishResource])

async def get(dishes_service: dishes_service_dep) -> list[DishResource]:
    result: list[Dish] | None = dishes_service.get()

    if result == None:
         raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND, 
                    detail="Item not found"
                )
    return cast(list[DishResource], result)


@router.post(
    path = "",
    status_code = status.HTTP_200_OK,
    response_model = DishResource
)
async def post(item: Dish, dishes_service: dishes_service_dep) -> DishResource: 
    result: Dish | None = dishes_service.add(cast(Dish, item))
    if result is None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, 
            detail="Item may already exists."
        )

    return cast(DishResource, result)
