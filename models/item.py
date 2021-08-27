class Item:
    def __init__(self, name: str, color: str, size: str):
        self.name = name.strip()
        self.color = color.strip()
        self.size = size.strip()
