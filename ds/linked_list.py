class Node:
    def __init__(self, value):
        self.value = value
        self.next = None  # ссылка на следующий узел


class LinkedList:
    def __init__(self):
        self.head = None  # первый узел
        self.size = 0

    def add_first(self, value):
        """Добавить в начало"""
        node = Node(value)
        node.next = self.head
        self.head = node
        self.size += 1

    def add_last(self, value):
        """Добавить в конец"""
        node = Node(value)
        if self.head is None:
            self.head = node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = node
        self.size += 1

    def remove(self, value):
        """Удалить первое вхождение значения. Вернуть True, если удалили"""
        current = self.head
        previous = None
        while current is not None:
            if current.value == value:
                if previous is None:
                    self.head = current.next
                else:
                    previous.next = current.next
                self.size -= 1
                return True
            previous = current
            current = current.next
        return False

    def find(self, value):
        """Есть ли значение в списке"""
        current = self.head
        while current is not None:
            if current.value == value:
                return True
            current = current.next
        return False

    def to_list(self):
        """Превратить в обычный список Питона (удобно для тестов)"""
        result = []
        current = self.head
        while current is not None:
            result.append(current.value)
            current = current.next
        return result

    def __len__(self):
        return self.size