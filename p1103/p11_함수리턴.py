# return : 함수호출로 값을 전달할 때 사용
def cal(a,b):
    return a+b  # 함수호출로 값을 전달

sum = cal(1,2)  # 함수호출
print(sum)

def func(a,b):
    a+b
    return  # 리턴값이 없으면 함수종료

def big(a,b):
    c = 0
    if a > b:
        return a
    else:
        return -1

print(big(10,2))
