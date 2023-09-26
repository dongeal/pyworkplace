메모 = {1: 1, 2: 1}
 
def f(n):
    if n in 메모:
        return 메모[n]
    else:
        output = f(n - 1) + f(n - 2)
        메모[n] = output  #한번 계산한건 다시 계산하지 않고 메모된 값 돌려줌
        return output
 
print(f(4))