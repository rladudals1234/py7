# 입력한 들자를 입력한 숫자만큼 반복 출력
# 안녕하세요 3

def s_print(str1, num):
    for i in range(num):
        print(str1)

# str1 = input("글자를 입력하시오>> ")
# num = int(input("반복횟수를 입력하시오>> "))

# for i in range(num):
#     print(str1)

# s_print(str1, num)

# 함수를 사용 cal(3개)
# 두수와 +-*/ 4개중에 1개를 입력받아
# 두수의 결과를 출력하시오.
# def cal(num1, num2, str1):
#     if str1 == "+":
#         print(num1+num2)
#     elif str1 == "-":
#         print(num1-num2)
#     elif str1 == "*":
#         print(num1*num2)
#     elif str1 == "/":
#         print(num1/num2)

# num1 = int(input("첫번째 숫자를 입력하세오:"))
# num2 = int(input("두번째 숫자를 입력하세오:"))
# str1 = input("원하는 사칙연산 기호를 입력하세요.(+,-,*,/)")
# 10    첫번째 숫자
# 2     두번째 숫자
# +     더하기(빼기인지 곱하기인지 매개변수로 받기)
# 12    결과값
# 결과값을 출력하시오.
# cal(num1,num2,str1)

# cal() 함수생성해서 입력받은 두 숫자사이의 합을 출력하시오.
# cal(1,10)
def cal(num1,num2):
    sum = 0
    # 1~10까지의 합이 출력되도록 구성
    for i in range(num1,num2+1):
        sum+=i
    # return sum
    print(sum)

# 함수호출
# 값을 출력하시오.
num1 = int(input("첫번째 숫자를 입력하세오:"))
num2 = int(input("두번째 숫자를 입력하세오:"))
# print(cal(num1,num2))
cal(num1,num2)
cal(2,10)
cal(5,9)
cal(11,20)
# 함수사용목적 - 반복제거, 유지보수 편의성, 코드관리 편의성
