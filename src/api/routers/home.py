from fastapi import APIRouter, status

router = APIRouter(
    tags=["home"]
)
    
@router.get(
        path = "/", 
        response_model = dict,
        status_code = status.HTTP_200_OK
    )

async def home() -> dict:
    return {"Hello": "Jovie"}