class Item:
    def __init__(self, text: str):
        self.text = text

    def __str__(self):
        return f"Task: {self.text}"
