
MOVE_MESSAGE = "{}번 원반을 {}에서 {}로 이동"

# def move(N, start, destination):
      
        # print(MOVE_MESSAGE.format(N, start, destination))
        
        
count = 0      
def hanoi(n, start, destination, via):
    
    global count
    # 원반이 1개일 때 시작 기둥에서 도착 기둥까지 한 번에 실질적인이동
    if n <= 1:
        print(MOVE_MESSAGE.format(n, start, destination))
        count += 1   # 실질적인 이동 카운트
        
    else :
        
    # 원반 n-1개를 시작 기둥에서 보조 기둥으로 이동하도록 함수를 다시 부름
        hanoi(n - 1, start, via, destination)
        
    # 가장 큰 원반을 시작 기둥에서 도착 기둥으로 실질적인 이동
        print(MOVE_MESSAGE.format(n, start, destination))
        count += 1  # 실질적인 이동 카운트
    
    # 원반 n-1개를 보조 기둥에서 도착 기둥으로 이동하도록 함수를 다시부름
        hanoi(n - 1, via, destination, start)
      

if __name__ == '__main__':
    
    tower_number = int(input('탑의수 :'))
  
    start = "출발지"
    destination = "목적지"
    via = "경유지"
    # print(p1)
    hanoi(tower_number, start, destination, via)
    print('총 이동 횟수:', count)
 
   
