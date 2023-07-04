
MOVE_MESSAGE = "{}번 원반을 {}에서 {}로 이동"

# def move(N, start, destination):
      
        # print(MOVE_MESSAGE.format(N, start, destination))
        
        # p1[N-1,start-1]=0
        # p1[N-1,destination-1]=N
        # p2=np.sort(p1,axis=0)
        # print(p2)
        
        # for h in range(0,tower_number):
        #     for w in range(0,3):
        #         img[100+h*10:110+h*10, 100+w*100:200+w*100]= t[p2[h,w]]
                
        #         cv2.imshow('hanoi', img)
       
        
        # cv2.waitKey(1500)
count = 0      
def hanoi(n, start, destination, via):
   
    global count
    # 원반이 1개일 때 시작 기둥에서 도착 기둥까지 한 번에 이동
    if n <= 1:
        print(MOVE_MESSAGE.format(n, start, destination))
        count += 1
        
    else :
        
    # 원반 n-1개를 시작 기둥에서 보조 기둥으로 이동
        hanoi(n - 1, start, via, destination)
        count += 1
    # 가장 큰 원반을 시작 기둥에서 도착 기둥으로 이동
    
        print(MOVE_MESSAGE.format(n, start, destination))
    
    # 원반 n-1개를 보조 기둥에서 도착 기둥으로 이동
        hanoi(n - 1, via, destination, start)
      
        # print(MOVE_MESSAGE.format(n, start, destination))    
   

if __name__ == '__main__':
    
    tower_number = int(input('탑의수 :'))
  
    start = "출발지"
    destination = "목적지"
    via = "경유지"
    # print(p1)
    hanoi(tower_number, start, destination, via)
    print('총 이동 횟수:', count)
 
   
