# Instructions:
# Stack: Sort Stack (⚡Interview Question)
# The sort_stack function takes a single argument, a Stack object.  The function should sort the elements in the stack in ascending order (the lowest value will be at the top of the stack) using only one additional stack.  The function should use the pop, push, peek, and is_empty methods of the Stack object.

# Note: This is a new function, not a method within the Stack class.

# This will use the Stack class we created in these coding exercises:
# 30, 31, 32


# To sort the stack, you should create a new, empty stack to hold the sorted elements.  Then, while the original stack is not empty, you should remove the top element from the original stack and compare it to the top element of the sorted stack.  If the top element of the sorted stack is greater than the current element, you should move the top element of the sorted stack back to the original stack until the current element is in the correct position.  Finally, you should add the current element to the sorted stack.

# Once all the elements have been sorted, you should copy the sorted elements from the sorted stack to the original stack in the correct order.

# Overall, the function should have a time complexity of O(n^2), where n is the number of elements in the original stack, due to the nested loops used to compare the elements.  However, the function should only use one additional stack, which could be useful in situations where memory is limited.


class Stack:
    def __init__(self):
        self.stack_list = []

    def print_stack(self):
        for i in range(len(self.stack_list)-1, -1, -1):
            print(self.stack_list[i])

    def is_empty(self):
        return len(self.stack_list) == 0

    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.stack_list[-1]

    def size(self):
        return len(self.stack_list)

    def push(self, value):
        self.stack_list.append(value)

    def pop(self):
        if self.is_empty():
            return None
        else:
            return self.stack_list.pop()




def sort_stack(stack):
    additional_stack = Stack()

    while not stack.is_empty():
        temp = stack.pop()

        while not additional_stack.is_empty() and additional_stack.peek() > temp:
            stack.push(additional_stack.pop())

        additional_stack.push(temp)

    while not additional_stack.is_empty():
        stack.push(additional_stack.pop())





my_stack = Stack()
my_stack.push(3)
my_stack.push(1)
my_stack.push(5)
my_stack.push(4)
my_stack.push(2)

print("Stack before sort_stack():")
my_stack.print_stack()

sort_stack(my_stack)

print("\nStack after sort_stack:")
my_stack.print_stack()

