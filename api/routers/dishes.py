from fastapi import APIRouter, status, HTTPException, Response

from api.routers.dish import DishResource
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
async def get():
    return dishes_service.get()


@router.post(
    path = "/",
    status_code = status.HTTP_200_OK,
    response_model = DishResource
)
async def post(item: DishResource): 
    return dishes_service.add(item)

