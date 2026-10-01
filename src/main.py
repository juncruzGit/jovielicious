
import uvicorn

from fastapi import Depends, FastAPI

from packages.api.routers import home, dishes, dish, dish_sizes, dish_size

app = FastAPI()

app.include_router(home.router)
app.include_router(dishes.router)
app.include_router(dish.router)
app.include_router(dish_sizes.router)
app.include_router(dish_size.router)

if __name__ == '__main__':
    uvicorn.run(
        "main:app", 
        host = "127.0.0.1", 
        port = 8000,
        reload = True
    )