# Instructions:
# LL: Reverse Between (⚡Interview Question)
# You are given a singly linked list and two integers m and n. Your task is to write a method reverse_between within the LinkedList class that reverses the nodes of the linked list from index m to index n (inclusive) in one pass and in-place.

# Input

# The method reverse_between takes two integer inputs m and n.

# The method will only be passed valid indexes (you do not need to test whether the indexes are out of bounds)



# Output

# The method should modify the linked list in-place by reversing the nodes from index m to index n.

# If the linked list is empty or has only one node, the method should return None.



# Example

# Suppose the linked list is 1 -> 2 -> 3 -> 4 -> 5, and m = 2 and n = 4. Then, the method should modify the linked list to 1 -> 2 -> 5 -> 4 -> 3 .



# Constraints

# The algorithm should run in one pass and in-place, with a time complexity of O(n) and a space complexity of O(1).

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
    
    def reverse_between(self, m, n):
        if not self.head:
            return None
        
        dummy = Node(0)
        dummy.next = self.head
        prev = dummy

        for i in range(m):
            prev = prev.next

        current = prev.next
        for i in range(n-m):
            temp = current.next
            current.next = temp.next
            temp.next = prev.next
            prev.next = temp

        self.head = dummy.next
    


my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)
my_linked_list.append(5)

my_linked_list.print_list()

print("\nReversed LL: ")
my_linked_list.reverse_between(2, 4)

my_linked_list.print_list()