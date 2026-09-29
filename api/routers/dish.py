from fastapi import APIRouter, status, HTTPException

from api.resources import DishResource
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
async def get(id : str):    
    dish = dish_service.get(id)
    if dish == None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail="Item not found"
        )
    else:
        return dish


@router.put(
        path = "/",
        status_code = status.HTTP_200_OK,
        response_model = DishResource
    )
async def put(item: DishResource) :
    dish = dish_service.modify(item)
    if (dish == None):
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND, 
            detail = "Item not found")
    else:
        return dish


@router.delete(
        path = "/", 
        status_code = status.HTTP_200_OK
    )
async def delete(id: str) :    
   dish_service.remove(id)
   return {
       "message": "Success"
    }
