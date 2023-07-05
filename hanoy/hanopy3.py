class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0


def hanoi_iterative(n, source, auxiliary, destination):
    stack = Stack()
    counter = 0

    # Push initial values to the stack
    stack.push((n, source, auxiliary, destination))

    while not stack.is_empty():
        n, source, auxiliary, destination = stack.pop()

        if n == 1:
            # Move the top disk from source to destination
            print(f"Move disk 1 from {source} to {destination}")
            counter += 1
        else:
            # Push subproblems to the stack
            stack.push((n - 1, auxiliary, source, destination))
          
            
            stack.push((1, source, auxiliary, destination))
            
            stack.push((n - 1, source, destination, auxiliary))
          
    return counter


# Example usage
num_disks = 3
moves = hanoi_iterative(num_disks, 'A', 'B', 'C')
print(f"\nTotal moves required: {moves}")
