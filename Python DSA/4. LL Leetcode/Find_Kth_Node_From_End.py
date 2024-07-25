# Instructions:
# LL: Find Kth Node From End (⚡Interview Question)
# Method name:
# find_kth_from_end

# Find the item that is a certain number of steps away from the end of the linked list WITHOUT USING LENGTH.

# For example, let's say you want to find the item that is 3 steps away from the end of the LL. To do this, you would start from the head of the LL and move through the links until you reach the item that is 3 steps away from the end.

# This is the problem of finding the "kth node from the end" of a linked list. Your task is to write a program that takes as input a linked list and a number k, and returns the item that is k steps away from the end of the list. If the linked list has fewer than k items, the program should return None.


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True
    
def find_kth_from_end(ll, k):
    slow = fast = ll.head
    for _ in range(k):
        if fast is None:
            return None
        fast = fast.next

    while fast:
        slow = slow.next
        fast = fast.next
    return slow.value


my_linked_list = LinkedList(0)
my_linked_list.append(1)
my_linked_list.append(2)
my_linked_list.append(3)

my_linked_list.print_list()

kth_number = find_kth_from_end(my_linked_list, 3)

print("\nThe kth number is: ", kth_number)

