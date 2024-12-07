class Jar:
    def __init__(self, capacity=12):
        if not isinstance(capacity, int) or capacity < 0:
            raise ValueError("Capacity must be a non-negative integer.")
        self._capacity = capacity
        self._size = 0

    def __str__(self):
        return "🍪" * self.size

    def deposit(self, n):
        if self._size + n > self.capacity:
            raise ValueError("Not enough space in the jar for that many cookies.")
        self._size += n

    def withdraw(self, n):
        if self._size - n < 0:
            raise ValueError("Not enough cookies in the jar to withdraw.")
        self._size -= n

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size
