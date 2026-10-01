
# import sys
# sys.path.append("/Users/Shared/Python")

# create a package
# from common.repository.shelve_repository import ShelveRepository 

from .shelve_repository import ShelveRepository
class DishRepository(ShelveRepository):

    def __init__(self):
        return super().__init__("Dishes")

    