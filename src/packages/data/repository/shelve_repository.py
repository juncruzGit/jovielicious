import shelve
import logging

class ShelveRepository():
    _name: str
    
    def __init__(self, name):
        self._name = name
        with shelve.open(self._name) as db:
            ...

    def insert(self, item: any): # type: ignore[type-abstract]
        with shelve.open(self._name) as db:
            if self.itemExist(item):
                logging.info(f"item {item} already exists.") 
            else:
                logging.info(f"item {item} is being added.")
                db[item.id.lower()] = item
                
        # return super().insert(item) # type: ignore

    def find(self, id: any) -> any: # type: ignore[type-abstract]
        with shelve.open(self._name) as db:
            item = db.get(id.lower())
            if item == None:
                print(f'No record found for {id}')
            else:
                return item
        # return super().find(id)

    def get(self, criteria: dict) -> list[any]: # type: ignore[type-abstract]
        with shelve.open(self._name) as db:
            if criteria == None:
                result = list(db.values())
                return result
            else:
                return None # type: ignore[type-abstract]


    def delete(self, id :any) -> bool: # type: ignore[type-abstract]
        with shelve.open(self._name) as db:
            if id in db:
                del db[id.lower()]
                print(f'{id} removed from record!')
            else:
                print (f'Record {id} no longer exists!')
    


    def itemExist(self, item : any) -> bool : # type: ignore[type-abstract]
        with shelve.open(self._name) as db:
            return item.name.lower() in db
        

    def update(self, item : any) -> any : # type: ignore[type-abstract]
        with shelve.open(self._name) as db:
            result: any = None # type: ignore[type-abstract]
            if item.id.lower() in db:
                db[item.id.lower()] = item
                print(f'Record {item.name} is updated.')
                result = item
            else:
                 print(f'No record found for {item.name}')