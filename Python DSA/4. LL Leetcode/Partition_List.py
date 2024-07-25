# Instructions:
# LL: Partition List (⚡Interview Question)
# You are given a singly linked list implementation in Python that does not have a tail pointer (which will make this method simpler to implement).

# You are tasked with implementing a method partition_list(self, x) that will take an integer x and partition the linked list such that all nodes with values less than x come before nodes with values greater than or equal to x. You should preserve the original relative order of the nodes in each of the two partitions.

# You need to implement this method as a method of the LinkedList class. The method should take an integer x as input. If the linked list is empty, the method should return None.

# To implement this method, you should create two new linked lists. These two linked lists will be made up of the original nodes from the linked list that is being partitioned, one for nodes less than x and one for nodes greater than or equal to x.  None of the nodes from the linked list should be duplicated.

# The creation of a limited number of new nodes is allowed (e.g., dummy nodes to facilitate the partitioning process).

# You should then traverse the original linked list and append each node to the appropriate new linked list.

# Finally, you should connect the two new linked lists together.

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
    
    def partition_list(self, x):
        if not self.head:
            return None
        
        dummy1 = Node(0)
        dummy2 = Node(0)
        prev1 = dummy1
        prev2 = dummy2

        current = self.head

        while current:
            if current.value < x:
                prev1.next = current
                prev1 = current
            else:
                prev2.next = current
                prev2 = current
            current = current.next

        prev2.next = None
        prev1.next = dummy2.next

        self.head = dummy1.next
    


my_linked_list = LinkedList(2)
my_linked_list.append(23)
my_linked_list.append(7)
my_linked_list.append(3)

my_linked_list.print_list()

print("\nPartitioning LL")

my_linked_list.partition_list(4)
my_linked_list.print_list()