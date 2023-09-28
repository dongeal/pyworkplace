# turtle로 음양 그리기

from turtle import *

def yinyang(c1,c2):
    begin_fill()
    circle(100,180)
    circle(200,180)
    circle(100,-180)
    color(c1)
    end_fill()
    
    up()
    rt(90)
    fd(50)
    rt(90)
    down()
    
    color(c2)
    begin_fill()
    circle(50, 360)
    end_fill()
    
    up()
    rt(90)
    fd(50)
    rt(90)
    down()

if __name__=="__main__":
    shape('circle')
    shapesize(.5)
    speed(9)
    yinyang('white','black')
     
    yinyang('black','white')
    
    ht()
  
mainloop()