from fastapi import APIRouter, status, HTTPException

from api.resources import DishSizeResource
from service.dish_sizes_service import DishSizesService

dish_sizes_service: DishSizesService = DishSizesService()

router = APIRouter(
    prefix = "/dishes/{id}/sizes/{size}", 
    tags = ["dish size"])

@router.get(
        path = "/", 
        response_model = DishSizeResource)
async def get(id: str, size: str):    
    result = dish_sizes_service.get_by_size(id, size)  
    if (result == None):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail="Dish not found")
    else:
        return result

@router.patch(
        path = "/", 
        status_code = status.HTTP_202_ACCEPTED, 
        response_model = list[DishSizeResource])
async def patch(id: str, size : str, updated_size: DishSizeResource):
    dish_sizes=dish_sizes_service.update_size(id, updated_size)  
    if (dish_sizes == None or 
        dish_sizes.count == 0):
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, 
                detail="Dish not found")
    else:
        return dish_sizes

@router.delete(
        path="/", 
        status_code=status.HTTP_200_OK)
async def delete(id: str, size: str ) :    
   dish_sizes_service.remove_size(id, size)
   return {
       "message": "Success"
    }