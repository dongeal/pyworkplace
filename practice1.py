class Badorder(Exception):
    pass

chicken = 10
waiting= 1

while True:
    try:
        print("[남은치킨은 {0}마리]".format(chicken))
        order = int(input("몇마리 주문하시겠 습니까? :"))
        if order > chicken :
            print ("재고가 부족합니다.")
        elif order <= 0:
            raise Badorder
        else:
            print("{0} 번 고객님 {1} 마리 주문 하셨습니다.".format(waiting, order))
            waiting += 1
            chicken -= order
        if chicken == 0:
            print("재고가 소진되었습니다.")
            break
    except ValueError:
        print ("잘못된 값을 입력하셨습니다.")
    except Badorder:
        print("주문이 잘못 되엇습니다.")