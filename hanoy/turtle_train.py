from turtle import *

class Disc(Turtle): # Disc 는 속성이 Turtle 임을선언.
    def __init__(self, n):
        Turtle.__init__(self, shape="square", visible=False)
        self.speed(6)
        self.penup()        # 이동줄 그리지 말고
        self.shapesize(1.5, n*1.5, 2) # (가로 세로 테두리)
        self.fillcolor(n/6., 0, 1-n/6.)
        self.showturtle()   # 이동중 터틀 보이기
        
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
    
def hanoi(n, from_, with_, to_):
    if n > 0:
        hanoi(n-1, from_, to_, with_)
        to_.push(from_.pop())
        hanoi(n-1, with_, from_, to_)


def play():
    onkey(None,"space")
    clear()
    try:
        hanoi(6, t1, t2, t3)
        write("press STOP button to exit",
              align="center", font=("Courier", 16, "bold"))
    except Terminator:
        pass  # turtledemo user pressed STOP


if __name__=="__main__":
    
    print(speed())
    hideturtle()
    penup()
    goto(0, -225)   

    t1 = Tower(-250)
    t2 = Tower(0)
    t3 = Tower(250)
    # make tower of 6 discs
    for i in range(6,0,-1):
        t1.push(Disc(i))
    # prepare spartanic user interface ;-)
    write("press spacebar to start game",
          align="center", font=("Courier", 16, "bold"))

    onkey(play, "space")
    listen()

mainloop()