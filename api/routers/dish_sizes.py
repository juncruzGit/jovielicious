from fastapi import APIRouter, status, HTTPException

from api.resources import DishSizeResource
from service.dish_sizes_service import DishSizesService

dish_sizes_service : DishSizesService = DishSizesService()

router = APIRouter(
    prefix = "/dishes/{id}/sizes",
    tags = ["dish sizes"])

@router.get(
        path="/",
        status_code=status.HTTP_200_OK,
        response_model=list[DishSizeResource])
async def get(id : str):    
    result=dish_sizes_service.get(id)  
   
    if (result == None or 
        result.count == 0):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail="Item not found"
        )
    else:
        return result
        
   
@router.put(
        path="/",
        status_code=status.HTTP_202_ACCEPTED,
        response_model=list[DishSizeResource])
async def put(id: str, item: DishSizeResource):
    result=dish_sizes_service.add_size(id, item)     
     
    if (result == None or 
        result.count == 0):
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND, 
            detail = "Item not found"
        )
    else:
        return result