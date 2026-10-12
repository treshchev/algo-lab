class Array:
    def __init__(self):
        self.data = []

    def append(self, value):
        """Добавить в конец"""
        self.data.append(value)

    def insert(self, index, value):
        """Вставить на позицию index"""
        self.data.insert(index, value)

    def remove_at(self, index):
        """Удалить элемент по номеру"""
        if index < 0 or index >= len(self.data):
            raise IndexError("Нет такого индекса")
        self.data.pop(index)

    def get(self, index):
        """Получить элемент по номеру"""
        if index < 0 or index >= len(self.data):
            raise IndexError("Нет такого индекса")
        return self.data[index]

    def set(self, index, value):
        """Заменить элемент по номеру"""
        if index < 0 or index >= len(self.data):
            raise IndexError("Нет такого индекса")
        self.data[index] = value

    def find(self, value):
        """Вернуть индекс значения или -1, если его нет"""
        for i in range(len(self.data)):
            if self.data[i] == value:
                return i
        return -1

    def __len__(self):
        return len(self.data)