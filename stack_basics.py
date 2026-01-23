class Stack:
    def __init__(self):
        self.stack = []

    # Push element into stack
    def push(self, item):
        self.stack.append(item)
        print(f"{item} pushed to stack")

    # Pop element from stack
    def pop(self):
        if self.is_empty():
            print("Stack is empty! Cannot pop.")
            return None
        return self.stack.pop()

    # Peek top element
    def peek(self):
        if self.is_empty():
            print("Stack is empty!")
            return None
        return self.stack[-1]

    # Check if stack is empty
    def is_empty(self):
        return len(self.stack) == 0

    # Get size of stack
    def size(self):
        return len(self.stack)


# Example usage
s = Stack()
s.push(10)
s.push(20)
s.push(30)

print("Top element:", s.peek())
print("Popped element:", s.pop())
print("Stack size:", s.size())
