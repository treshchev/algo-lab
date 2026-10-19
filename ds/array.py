class Array:
    def __init__(self):
        self.data = []

    def append(self, value):
        self.data.append(value) # добавляем в конец

    def insert(self, index, value):
        self.data.insert(index, value) # позиция на index

    def remove_at(self, index):
        if index < 0 or index >= len(self.data):
            raise IndexError("Нет такого индекса") # по номеру удалить элмент
        self.data.pop(index)

    def get(self, index):
        if index < 0 or index >= len(self.data):
            raise IndexError("Нет такого индекса") # получить по номеру элемент
        return self.data[index]

    def set(self, index, value):
        if index < 0 or index >= len(self.data):
            raise IndexError("Нет такого индекса") # заменить по номеру
        self.data[index] = value

    def find(self, value):
        for i in range(len(self.data)):
            if self.data[i] == value:
                return i
        return -1 # вернуть индекс или -1 если нету такого

    def __len__(self):
        return len(self.data)