from my_stack_array import Stack

stack = Stack()

stack.put(10)
stack.put(20)
stack.put(30)
stack.put(40)

print("Stack:", stack.data)
print("Top index:", stack.top)

print("Peek:", stack.peek())

print("Removed:", stack.remove())

print("Stack:", stack.data)
print("Top index:", stack.top)

print("Is empty:", stack.is_empty())
print("Removed:", stack.remove())