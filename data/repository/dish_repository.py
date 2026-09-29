from common.repository.shelve_repository import ShelveRepository

class DishRepository(ShelveRepository):

    def __init__(self):
        return super().__init__("Dishes")

    