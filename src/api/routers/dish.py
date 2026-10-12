from typing import cast
from fastapi import APIRouter, status, HTTPException

from src import Dish, DishResource, Routes
from ...dependencies import dish_service_dep

router = APIRouter(
    prefix = Routes.dish,
    tags = ["dish"])

@router.get(
        path = "",
        status_code = status.HTTP_200_OK,
        response_model = DishResource
        )
async def get(id: str, dish_service: dish_service_dep) -> DishResource:
    dish: Dish = dish_service.get(id)
    if dish is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail="Item not found"
        )
    else:
        return cast(DishResource, dish)


@router.put(
        path = "",
        response_model=DishResource,
        status_code = status.HTTP_200_OK
    )
async def put(item: Dish, dish_service: dish_service_dep) -> DishResource :
    dish: Dish | None = dish_service.modify(cast(Dish, item))
    if (dish is None):
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND, 
            detail = "Item not found")
    else:
        return cast(DishResource, dish)


@router.delete(
        path = "", 
        response_model = dict,
        status_code = status.HTTP_200_OK
    )
async def delete(id: str, dish_service: dish_service_dep) -> dict:    
   successful: bool = dish_service.remove(id)

   if (not successful):
        raise HTTPException(
            status_code = status.HTTP_400_BAD_REQUEST, 
            detail = "Item not found.")
   
   return {
       "message": "Success"
    }
