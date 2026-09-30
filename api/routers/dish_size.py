from typing import cast

from fastapi import APIRouter, status, HTTPException

from api.resources import DishSizeResource
from data.model.dish_size import DishSize
from service.dish_sizes_service import DishSizesService

dish_sizes_service: DishSizesService = DishSizesService()

router = APIRouter(
    prefix = "/dishes/{id}/sizes/{size}", 
    tags = ["dish size"])

@router.get(
        path = "/", 
        response_model = DishSizeResource)
async def get(id: str, size: str) -> DishSizeResource:    
    result: DishSize | None = dish_sizes_service.get_by_size(id, size)  
    if (result is None):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail="Dish not found")
    else:
        return cast(DishSizeResource, result)

@router.patch(
        path = "/", 
        status_code = status.HTTP_202_ACCEPTED, 
        response_model = list[DishSizeResource])
async def patch(id: str,
                size: str,
                updated_size: DishSizeResource) -> list[DishSizeResource]:

    if size != updated_size.size:
        raise HTTPException(
                status_code = status.HTTP_400_BAD_REQUEST, 
                detail = f"Updated size name is not equal to {size}") 

    dish_sizes: list[DishSize] | None = dish_sizes_service.update_size(id, updated_size)  
    if (dish_sizes is None or 
        dish_sizes.count == 0):
            raise HTTPException(
                status_code = status.HTTP_404_NOT_FOUND, 
                detail = "Dish not found")
    else:
        return cast(list[DishSizeResource], dish_sizes)


@router.delete(
        path = "/", 
        status_code = status.HTTP_200_OK)
async def delete(id: str, size: str ) -> dict :    
   dish_sizes_service.remove_size(id, size)
   return {
       "message": "Success"
    }