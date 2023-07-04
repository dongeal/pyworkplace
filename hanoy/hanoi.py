# import cv2
# from cv2 import waitKey
import numpy as np

# img = cv2.imread('base.jpg')
# t=['t0.jpg', 't1.jpg', 't2.jpg', 't3.jpg', 't4.jpg','t5.jpg']
# for i in range(0,6):
#     t[i] = cv2.imread(t[i])
   
#     # img[100+i*10:110+i*10, 100:200]= t[i]

# cv2.imshow('hanoi', img)



MOVE_MESSAGE = "{}번 원반을 {}에서 {}로 이동"



def move(N, start, destination):
      
        print(MOVE_MESSAGE.format(N, start, destination))
        
        p1[N-1,start-1]=0
        p1[N-1,destination-1]=N
        p2=np.sort(p1,axis=0)
        print(p2)
        
        # for h in range(0,tower_number):
        #     for w in range(0,3):
        #         img[100+h*10:110+h*10, 100+w*100:200+w*100]= t[p2[h,w]]
                
        #         cv2.imshow('hanoi', img)
       
        
        # cv2.waitKey(1500)
       
def hanoi(n, start, destination, via):
   
    global count
    # 원반이 1개일 때 시작 기둥에서 도착 기둥까지 한 번에 이동
    if n <= 1:
        move(1, start, destination)
        return 1

    count = 0
    # 원반 n-1개를 시작 기둥에서 보조 기둥으로 이동
    count += hanoi(n - 1, start, via, destination)

    # 가장 큰 원반을 시작 기둥에서 도착 기둥으로 이동
    count += 1
    move(n, start, destination)

    # 원반 n-1개를 보조 기둥에서 도착 기둥으로 이동
    count += hanoi(n - 1, via, destination, start)
    print("{} 번째이동".format(count))
    
    return count


if __name__ == '__main__':
    global p1
    global p2
    tower_number = int(input('탑의수 :'))
    
    p1=np.zeros(shape=(tower_number,3),dtype=np.uint8)
    print(p1)
    for i in range(0,tower_number):
        p1[i,0] = i+1 
    # for h in range(0,tower_number):
    #         for w in range(0,3):
    #             img[100+h*10:110+h*10, 100+w*100:200+w*100]= t[p1[h,w]]
    #             cv2.imshow('hanoi', img)   
    # cv2.waitKey(0) 
    # p1= np.array([[1,0,0],[2,0,0],[3,0,0]])
    # print(p1)

    start = 1
    destination = 3
    via = 2
    # print(p1)
    total_count = hanoi(tower_number, start, destination, via)
    print('총 이동 횟수:', total_count)
 
    # cv2,waitKey(0)
    # cv2.destroyAllWindows()
