# input() 함수
# 문자열을 입력받는 함수, 입력받는 모든 것은 문자열 타입
# 문자열 + 숫자 : 불가능

"""a = input("숫자를 입력하세요: ") #str타입 - 입력받는 모든 것 문자열 타입
print("숫자에 200을 더하면: "+str(int(a)+200))"""

# ctrl-/로 주석처리
# input1 = input("이름을 입력하세요: ")
# input2 = input("나이를 입력하세요: ") #숫자를 입력받아도 문자열타입
# print("이름: "+input1, "나이: "+input2)

### num1,num2 2개를 입력받아 숫자타입으로 변경 후 사칙연산 결과를 출력하시오.
### int(num)
# num1 = input("첫번째 숫자를 입력하세요: ")
# num2 = input("두번째 숫자를 입력하세요: ")
num1, num2 = input("첫번째 숫자를 입력하세요: "), input("두번째 숫자를 입력하세요: ")
print("더하기연산결과: "+str(int(num1)+int(num2)))
print("빼기연산결과: "+str(int(num1)-int(num2)))
print("곱하기연산결과: "+str(int(num1)*int(num2)))
print("나누기연산결과: "+str(int(num1)/int(num2)))
print("나눈 나머지: ",end="")
print(int(num1)%int(num2))
