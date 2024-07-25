# Instructions:
# DLL: Swap First and Last (⚡Interview Question)
# Swap the values of the first and last node

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1
        return True
    
    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def swap_first_last(self):
        if self.head is None or self.head == self.tail:
            return
        # temp = self.head.value
        # self.head.value = self.tail.value
        # self.tail.value = temp
        self.head.value, self.tail.value = self.tail.value, self.head.value


my_dll = DoublyLinkedList(3)
my_dll.append(2)
my_dll.append(4)
my_dll.append(9)

my_dll.print_list()

my_dll.swap_first_last()

print("\nAfter swapped:")
my_dll.print_list()

