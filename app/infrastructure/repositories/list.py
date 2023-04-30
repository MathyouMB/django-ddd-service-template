from app.infrastructure.db.models import List as ListModel, Item as ItemModel
from app.domain import List, Item
from app.error import Error, ErrorType
from result import Ok, Err, Result


class ListRepository:
    def find_by_id(self, list_id) -> Result[List, Error]:
        try:
            list_record = ListModel.objects.get(id=list_id)
            list = self.convert_list_model_to_list_domain(list_record)
            return Ok(list)
        except ListModel.DoesNotExist:
            return Err(Error("List does not exist", ErrorType.RECORD_NOT_FOUND))

    def save(self, list: List) -> Result[List, Error]:
        try:
            return Ok(self.convert_list_domain_to_list_model(list))
        except Exception as e:
            return Err(Error(str(e), ErrorType.FAILED_TO_CREATE))

    def convert_item_model_to_item_domain(self, item: ItemModel) -> Item:
        return Item(text=item.text)

    def convert_list_model_to_list_domain(self, list: ListModel) -> List:
        items = []

        for i in list.items():
            items.append(self.convert_item_model_to_item_domain(i))

        return List(id=int(list.id), name=list.name, items=items)

    def convert_item_domain_to_item_model(
        self, item: Item, list: ListModel
    ) -> ItemModel:
        item_record, _ = ItemModel.objects.get_or_create(text=item.text, list=list)

        return item_record

    def convert_list_domain_to_list_model(self, l: List) -> ListModel:
        list_record, _ = ListModel.objects.get_or_create(id=l.id, name=l.name)

        for i in l.items:
            self.convert_item_domain_to_item_model(i, list_record)

        return list_record
