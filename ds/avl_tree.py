class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.height = 1  # высота узла лист = 1


class AVLTree:
    def __init__(self):
        self.root = None
    def _height(self, node):
        if node is None:
            return 0
        return node.height

    def _update_height(self, node):
        node.height = 1 + max(self._height(node.left), self._height(node.right))

    def _balance(self, node):
        if node is None:
            return 0
        return self._height(node.left) - self._height(node.right) # высота левого отнять высоту правого, баланс

    def _rotate_right(self, y):
        x = y.left
        y.left = x.right
        x.right = y
        self._update_height(y)  # сначала нижний узел
        self._update_height(x)
        return x  # x теперь наверху

    def _rotate_left(self, x):
        y = x.right
        x.right = y.left
        y.left = x
        self._update_height(x)
        self._update_height(y)
        return y  # y теперь наверху

    def _rebalance(self, node):
        self._update_height(node)
        balance = self._balance(node)

        if balance > 1:  # перекос влево
            if self._balance(node.left) < 0:  # влево вправо
                node.left = self._rotate_left(node.left)
            return self._rotate_right(node)

        if balance < -1:  # перекос вправо
            if self._balance(node.right) > 0:  # наоборот
                node.right = self._rotate_right(node.right)
            return self._rotate_left(node)

        return node

    def insert(self, value):
        self.root = self._insert(self.root, value) # добавить значение в древо

    def _insert(self, node, value):
        if node is None:
            return Node(value)
        if value < node.value:
            node.left = self._insert(node.left, value)
        elif value > node.value:
            node.right = self._insert(node.right, value)
        else:
            return node  # дубликат не добавляем
        return self._rebalance(node)  # после вставки проверяем баланс

    def find(self, value):
        node = self.root
        while node is not None:
            if value == node.value:
                return True
            if value < node.value:
                node = node.left
            else:
                node = node.right
        return False

    def height(self):
        return self._height(self.root)

    def to_list(self):
        result = []
        self._in_order(self.root, result)
        return result

    def _in_order(self, node, result):
        if node is None:
            return
        self._in_order(node.left, result)
        result.append(node.value)
        self._in_order(node.right, result)