
import logging.config

from dependency_injector import containers, providers
from dependency_injector.wiring import Provide, inject
from .data.repository.dish_repository import DishRepository

class Container(containers.DeclarativeContainer):
    config = providers.Configuration(ini_files=["config.ini"])

    logging = providers.Resource(
        logging.config.fileConfig,  
        fname="logging.ini",
    )

    dish_repository = providers.Factory(DishRepository)

    
    