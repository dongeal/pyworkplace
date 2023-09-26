import turtle as t
t.shape()
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


def hanoi_iterative(n, disk_no, source, auxiliary, destination):
    stack = Stack()
    counter = 0
    

    # Push initial values to the stack
    stack.push((n, disk_no, source, auxiliary, destination))

    while not stack.is_empty():
        n, disk_no, source, auxiliary, destination = stack.pop()

        if n == 1:
            # Move the top disk from source to destination
            print(f"count: {counter+1} Move disk {disk_no}  from {source} to {destination}")
            counter += 1
        else:
            # Push subproblems to the stack
            stack.push((n-1, disk_no-1, auxiliary, source, destination))
            stack.push((1, disk_no, source, auxiliary, destination))
            stack.push((n-1, disk_no-1,source, destination, auxiliary))
            
    return counter


# Example usage
if __name__ == '__main__':
    num_disks = int(input('탑의수 :'))
   
    disk_no = num_disks

    moves = hanoi_iterative(num_disks, disk_no,'출발지', '경유지', '목적지')
    print(f"\nTotal moves required: {moves}")
    t.mainloop()