from turtle import *

def switchupdown(x=0, y=0):                
    if pen()["pendown"]:                                                     
        end_fill()                                               
        up()                                                                                                                                                           
    else:                                                                                                                      
        down()                                                                                                                                               
        begin_fill()                                                                                                                           

def changecolor(x=0, y=0):
    global colors                                                                                              
    colors = colors[1:]+colors[:1]                                                                                         
    color(colors[0])
                                 
def main():
    global colors                                                                                              
    shape("circle")                                                                                                           
    resizemode("user")

# 펜의 크기 변경 모드 설정하는 것으로
#  "auto", "user", "noresize" 가 있으며 기본은 "noresize"
# resizemode는 shapesize와 함께 사용됨(크기변경을 하려면 "user"로)
    shapesize(.5)                                         
# shapesize는 (너비, 길이, 외곽선) 
# 기본은(1, 1, 1)
    width(3)                                                                                                                                            
    colors=["red", "green", "blue", "yellow"]                                  
    color(colors[0])                                                                                                                          
    switchupdown()  
    onscreenclick(goto,1)                             
# goto 는 좌표이동(클릭한 곳으로 감)
# 명령어 뒤의 숫자는 1 : 마우스왼쪽버튼 , 2 : 마우스가운데버튼, 3 : 마우스오른쪽버튼
# 마우스 왼쪽버튼을 누르면 커서가 그곳으로 이동함

    onscreenclick(changecolor,2)                                                                  
    onscreenclick(switchupdown,3)                                                                  

    return "EVENTLOOP"                                                                                                           

if __name__ == "__main__":
    msg = main()                                                                                    
    print(msg)                                                                                                                                                 

    mainloop()                                          
