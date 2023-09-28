from turtle import *

class Disc(Turtle): # Disc 는 속성이 Turtle 임을선언.
    def __init__(self, n):
        Turtle.__init__(self, shape="square", visible=False)
        self.speed(6)
        self.penup()        # 이동줄 그리지 말고
        self.shapesize(1.5, n*1.5, 2) # (가로 세로 테두리)
        self.fillcolor(n/no_disc, 0, 1-n/no_disc)
        self.showturtle()   # 이동중 터틀 보이기
        self.sety(300)
class Tower(list): # Tower 는 list 임을 선언.
    "Hanoi tower, a subclass of built-in type list"
    def __init__(self, x):
        "create an empty tower. x is x-position of peg"
        self.x = x
    def push(self, disc): #Disc(사실상 터틀커서) setx, sety 에 그려 넣기
        disc.setx(self.x)
        disc.sety(-150+34*len(self))
        self.append(disc)
        
    def pop(self):       #Disc(사실상 터틀커서) 들어 올리기
        disc = list.pop(self)
        disc.sety(150) # 디스크 pop 할때 들어올릴 y 좌표
    
        return disc

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
            # print(f"count: {counter+1} Move disk {disk_no}  from {source} to {destination}")
            destination.push(source.pop())
            counter += 1
        else:
            # Push subproblems to the stack
            stack.push((n-1, auxiliary, source, destination))
            stack.push((1, source, auxiliary, destination))
            stack.push((n-1,source, destination, auxiliary))
            
    return counter


# # Example usage
# if __name__ == '__main__':
#     num_disks = int(input('탑의수 :'))
   
#     disk_no = num_disks

#     moves = hanoi_iterative(num_disks, disk_no,'출발지', '경유지', '목적지')
#     print(f"\nTotal moves required: {moves}")
    
# def hanoi(n, from_, with_, to_):
#     if n > 0:
#         hanoi(n-1, from_, to_, with_)
#         to_.push(from_.pop())
#         hanoi(n-1, with_, from_, to_)


def play():
    onkey(None,"space")
    clear()
    try:
        hanoi_iterative(no_disc, t1, t2, t3)
        write("press spacebar to exit",
              align="center", font=("Courier", 16, "bold"))
        onkey(quit,"space")
    except Terminator:
        pass  # turtledemo user pressed STOP


if __name__=="__main__":
   
    no_disc =int(textinput("탑의 수", "탑의수:"))
    hideturtle()
    penup()
    goto(0, -225)   
    
    
    t1 = Tower(-250)
    t2 = Tower(0)
    t3 = Tower(250)
    # make tower of 6 discs
    for i in range(no_disc,0,-1):
        t1.push(Disc(i))
    # prepare spartanic user interface ;-)
    write("press spacebar to start game",
          align="center", font=("Courier", 16, "bold"))

    onkey(play , "space")
    listen()

mainloop()