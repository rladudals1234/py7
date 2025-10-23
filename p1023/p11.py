### num1,num2 2개를 입력받아 숫자타입으로 변경 후 사칙연산 결과를 출력하시오.
### int(num)
# print(input("첫번째 숫자를 입력하세요: "))
# print(input("두번째 숫자를 입력하세요: "))

def plus(num1, num2):
    return str(num1+num2)

num1 = int(input("첫번째 숫자를 입력하세요: "))
num2 = int(input("두번째 숫자를 입력하세요: "))
print("더하기연산결과: "+plus(num1,num2))
print("빼기연산결과: "+str(num1-num2))
print("곱하기연산결과: "+str(num1*num2))
print("나누기연산결과: "+str(num1/num2))
print("나눈 나머지: ",end=""), print(num1%num2)
