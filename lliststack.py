"""Implementation of the Stack ADT using a singly linked list."""

class Stack:
    """Creates an empty stack."""
    def __init__(self):
        """Initialize new Stack."""
        self._top = None
        self._size = 0

    def isEmpty(self):
        """Returns True if the stack is empty or False otherwise."""
        return self._top is None

    def __len__(self):
        """Returns the number of items in the stack."""
        return self._size

    def peek(self):
        """Returns the top item on the stack without removing it."""
        assert not self.isEmpty(), "Cannot peek at an empty stack"
        return self._top.data

    def pop(self):
        """Removes and returns the top item on the stack."""
        assert not self.isEmpty(), "Cannot pop from an empty stack"
        node = self._top
        self._top = self._top.next
        self._size -= 1
        return node.data

    def push(self, data):
        """Pushes an item onto the top of the stack."""
        self._top = Node(data, self._top)
        self._size += 1

class Node:
    """The private storage class for creating stack nodes."""
    def __init__(self, data, link):
        """Initialize Node."""
        self.data = data
        self.next = link
