from app.domain.item import Item


class List:
    def __init__(self, id: str, name: str, items: list[Item]):
        self.id = id
        self.name = name
        self.items = items

    def add_item(self, item: Item):
        self.items.append(item)
