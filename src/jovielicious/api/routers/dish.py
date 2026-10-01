from typing import cast
from fastapi import APIRouter, status, HTTPException

from api.resources import DishResource
from data.model.dish import Dish
from service.dish_service import DishService

dish_service : DishService = DishService()

router = APIRouter(
    prefix = "/dishes/{id}",
    tags = ["dish"])

@router.get(
        path = "",
        status_code = status.HTTP_200_OK,
        response_model = DishResource
        )
async def get(id: str) -> DishResource:
    dish: Dish = dish_service.get(id)
    if dish is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail="Item not found"
        )
    else:
        return cast(DishResource, dish)


@router.put(
        path = "/",
        status_code = status.HTTP_200_OK,
        response_model = DishResource
    )
async def put(item: DishResource) -> DishResource :
    dish: Dish = dish_service.modify(cast(Dish,item))
    if (dish is None):
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND, 
            detail = "Item not found")
    else:
        return cast(DishResource, dish)


@router.delete(
        path = "/", 
        status_code = status.HTTP_200_OK
    )
async def delete(id: str) -> dict:    
   dish_service.remove(id)
   return {
       "message": "Success"
    }
