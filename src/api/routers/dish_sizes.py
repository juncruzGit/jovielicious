from typing import cast
from fastapi import APIRouter, status, HTTPException

from src import Routes, DishSizeResource, DishSize
from ...dependencies import dish_sizes_service_dep


router = APIRouter(prefix = Routes.dish_sizes, tags = ["dish sizes"])

@router.get(path = "", status_code = status.HTTP_200_OK,
            response_model = list[DishSizeResource])
async def get(id: str, 
              dish_sizes_service: dish_sizes_service_dep) -> list[DishSizeResource]:    
    result: list[DishSize] | None = dish_sizes_service.get(id)  
   
    if (result is None or 
        result.count == 0):
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND, 
            detail = "Item not found"
        )
    else:
        return cast(list[DishSizeResource], result)
        
   
@router.put(path = "", status_code = status.HTTP_202_ACCEPTED,
            response_model = list[DishSizeResource])
async def put(id: str, item: DishSizeResource, 
              dish_sizes_service: dish_sizes_service_dep) -> list[DishSizeResource]:
    result: list[DishSize] | None = dish_sizes_service.add_size(id, DishSize(**item.model_dump()))
     
    if (result is None or 
        result.count == 0):
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND, 
            detail = "Item not found"
        )
    else:
        return cast(list[DishSizeResource], result)