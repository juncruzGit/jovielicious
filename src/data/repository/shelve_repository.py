import shelve

class ShelveRepository():
    _name: str
    
    def __init__(self, name):
        self._name = name
        with shelve.open(self._name) as db:
            ...

    def insert(self, item: any) -> any | None: # type: ignore[type-abstract]
        with shelve.open(self._name) as db:
            if self.itemExist(item):
               return None
            else:
                db[item.id.lower()] = item
                return item
  

    def find(self, id: any) -> any: # type: ignore[type-abstract]
        with shelve.open(self._name) as db:
            item = db.get(id.lower())
            if item == None:
                print(f'No record found for {id}')
            else:
                return item


    def get(self, criteria: dict | None = None) -> list[any] | None: # type: ignore[type-abstract]
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
                return True
            else:
               return False
    

    def itemExist(self, item : any) -> bool : # type: ignore[type-abstract]
        with shelve.open(self._name) as db:
            return item.name.lower() in db
        

    def update(self, item : any) -> any | None : # type: ignore[type-abstract]
        with shelve.open(self._name) as db:
            if item.id.lower() in db:
                db[item.id.lower()] = item
                return item
            else:
                return None