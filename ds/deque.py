class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None  # ссылка на предыдущий узел
        self.next = None  # ссылка на следующий узел для себя


class Deque:
    def __init__(self):
        self.head = None  # первый узел
        self.tail = None  # последний узел
        self.size = 0

    def push_front(self, value):
        node = Node(value) # добавит в начало
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node
        self.size += 1

    def push_back(self, value):
        node = Node(value) # добавит в конце
        if self.tail is None:
            self.head = node
            self.tail = node
        else:
            node.prev = self.tail
            self.tail.next = node
            self.tail = node
        self.size += 1

    def pop_front(self):
        if self.head is None:
            raise IndexError("Дек пустой") # получить элемент из начала
        value = self.head.value
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        else:
            self.head.prev = None
        self.size -= 1
        return value

    def pop_back(self):
        if self.tail is None:
            raise IndexError("Дек пустой") # получить элемент из конца
        value = self.tail.value
        self.tail = self.tail.prev
        if self.tail is None:
            self.head = None
        else:
            self.tail.next = None
        self.size -= 1
        return value

    def peek_front(self):
        if self.head is None:
            raise IndexError("Дек пустой") # посмотреть 1 элмент
        return self.head.value

    def peek_back(self):
        if self.tail is None:
            raise IndexError("Дек пустой") 
        return self.tail.value # посмотреть последний элмент

    def is_empty(self):
        return self.size == 0

    def to_list(self):
        result = []
        current = self.head
        while current is not None:
            result.append(current.value)
            current = current.next
        return result

    def __len__(self):
        return self.size