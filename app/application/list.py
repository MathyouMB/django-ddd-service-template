from app.domain import List, Item
from app.infrastructure.repositories import ListRepository
from app.error import Error
from result import Ok, Result


class List:
    def __init__(self):
        self.list_repository = ListRepository()

    def find(self, list_id: str) -> Result[List, Error]:
        list_result = self.list_repository.find_by_id(list_id)
        return list_result

    def create_item(
        self,
        text: str,
        list_id: str,
    ) -> Result[Item, Error]:
        # find the existing list
        list_result = self.list_repository.find_by_id(list_id)

        # if list was not found, return error
        if list_result.is_err():
            return list_result

        # pull out the list domain object
        list = list_result.ok()

        # create the new item
        item = Item(text=text)

        # add the item to the list
        list.add_item(item)

        # save the aggregate
        save_result = self.list_repository.save(list)

        if save_result.is_err():
            return save_result

        return Ok(item)
