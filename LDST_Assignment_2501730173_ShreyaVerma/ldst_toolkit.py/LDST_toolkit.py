# -------------------------------
# Dynamic Array Implementation
# -------------------------------

class DynamicArray:
    def __init__(self, capacity=2):
        self.capacity = capacity
        self.size = 0
        self.arr = [None] * self.capacity

    def append(self, x):
        if self.size == self.capacity:
            self._resize()

        self.arr[self.size] = x
        self.size += 1

    def _resize(self):
        print(f"Resizing from {self.capacity} to {self.capacity * 2}")
        new_capacity = self.capacity * 2
        new_arr = [None] * new_capacity

        for i in range(self.size):
            new_arr[i] = self.arr[i]

        self.arr = new_arr
        self.capacity = new_capacity

    def pop(self):
        if self.size == 0:
            return "Array is empty"

        val = self.arr[self.size - 1]
        self.arr[self.size - 1] = None
        self.size -= 1
        return val

    def display(self):
        print([self.arr[i] for i in range(self.size)])


# -------------------------------
# Singly Linked List
# -------------------------------

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, x):
        new_node = Node(x)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, x):
        new_node = Node(x)

        if not self.head:
            self.head = new_node
            return

        temp = self.head
        while temp.next:
            temp = temp.next

        temp.next = new_node

    def delete_by_value(self, x):
        temp = self.head

        if temp and temp.data == x:
            self.head = temp.next
            return

        prev = None
        while temp and temp.data != x:
            prev = temp
            temp = temp.next

        if not temp:
            print("Value not found")
            return

        prev.next = temp.next

    def traverse(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")


# -------------------------------
# Doubly Linked List
# -------------------------------

class DNode:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, x):
        new_node = DNode(x)

        if not self.head:
            self.head = new_node
            return

        temp = self.head
        while temp.next:
            temp = temp.next

        temp.next = new_node
        new_node.prev = temp

    def insert_after(self, target, x):
        temp = self.head

        while temp and temp.data != target:
            temp = temp.next

        if not temp:
            print("Target not found")
            return

        new_node = DNode(x)
        new_node.next = temp.next
        new_node.prev = temp

        if temp.next:
            temp.next.prev = new_node

        temp.next = new_node

    def delete_at_position(self, pos):
        if not self.head:
            return

        temp = self.head

        if pos == 0:
            self.head = temp.next
            if self.head:
                self.head.prev = None
            return

        for _ in range(pos):
            temp = temp.next
            if not temp:
                return

        if temp.prev:
            temp.prev.next = temp.next

        if temp.next:
            temp.next.prev = temp.prev

    def traverse(self):
        temp = self.head
        while temp:
            print(temp.data, end=" <-> ")
            temp = temp.next
        print("None")


# -------------------------------
# Stack using Linked List
# -------------------------------

class Stack:
    def __init__(self):
        self.top = None

    def push(self, x):
        new_node = Node(x)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if not self.top:
            return "Stack Underflow"

        val = self.top.data
        self.top = self.top.next
        return val

    def peek(self):
        if not self.top:
            return "Empty Stack"
        return self.top.data


# -------------------------------
# Queue using Linked List
# -------------------------------

class Queue:
    def __init__(self):
        self.front_node = None
        self.rear = None

    def enqueue(self, x):
        new_node = Node(x)

        if not self.rear:
            self.front_node = self.rear = new_node
            return

        self.rear.next = new_node
        self.rear = new_node

    def dequeue(self):
        if not self.front_node:
            return "Queue Underflow"

        val = self.front_node.data
        self.front_node = self.front_node.next

        if not self.front_node:
            self.rear = None

        return val

    def front(self):
        if not self.front_node:
            return "Empty Queue"
        return self.front_node.data


# -------------------------------
# Balanced Parentheses Checker
# -------------------------------

def is_balanced(expr):
    stack = Stack()
    pairs = {')': '(', '}': '{', ']': '['}

    for char in expr:
        if char in "({[":
            stack.push(char)
        elif char in ")}]":
            if not stack.top:
                return False
            if stack.pop() != pairs[char]:
                return False

    return stack.top is None


# -------------------------------
# MAIN TESTING
# -------------------------------

if __name__ == "__main__":
    print("---- Dynamic Array ----")
    da = DynamicArray(2)
    for i in range(10):
        da.append(i)
        da.display()

    print("Pop:", da.pop())
    print("Pop:", da.pop())
    print("Pop:", da.pop())
    da.display()

    print("\n---- Singly Linked List ----")
    sll = SinglyLinkedList()
    sll.insert_at_beginning(3)
    sll.insert_at_beginning(2)
    sll.insert_at_beginning(1)
    sll.insert_at_end(4)
    sll.insert_at_end(5)
    sll.traverse()

    sll.delete_by_value(3)
    sll.traverse()

    print("\n---- Doubly Linked List ----")
    dll = DoublyLinkedList()
    dll.insert_at_end(1)
    dll.insert_at_end(2)
    dll.insert_at_end(3)
    dll.insert_after(2, 5)
    dll.traverse()

    dll.delete_at_position(1)
    dll.traverse()

    print("\n---- Stack ----")
    st = Stack()
    st.push(10)
    st.push(20)
    print("Peek:", st.peek())
    print("Pop:", st.pop())

    print("\n---- Queue ----")
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    print("Front:", q.front())
    print("Dequeue:", q.dequeue())

    print("\n---- Parentheses Checker ----")
    tests = ["([])", "([)]", "(((", ""]
    for t in tests:
        print(t, "->", "Balanced" if is_balanced(t) else "Not Balanced")