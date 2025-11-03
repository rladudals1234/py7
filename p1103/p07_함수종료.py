def cal(a,b):   # 함수를 호출한 곳으로 값을 전달할때 사용(반환값)
    print(a+b)  # 함수끝을 만나면 함수종료됨.

cal(10,5)

def cal(a,b):   # 함수를 호출한 곳으로 값을 전달할때 사용(반환값)
    return a+b  # return을 만나면 함수종료

print(cal(2,7))

sum = cal(3,5)
print(sum)

# 3개의 계산 더하기,빼기를 구하시오.
num1 = cal(10,5)
num2 = cal(2,7)
num3 = cal(3,5)
print(num1+num2+num3)
print(num1-num2-num3)

