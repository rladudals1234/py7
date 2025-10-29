# for문 while문
# for 변수 in 범위:
# while 조건:
# for i in range(10):
#     print(i)

# i = 0           # 초기값
# while i<10:     # 조건식 - 조건이 맞을때까지 계속실행
#     print(i)
#     i = i + 1   # 증감식

# i = 1
# while(i != 0):
#     i = int(input("숫자를 입력하세요.(0 입력 : 종료)"))
#     print("입력한 값 : ",i)
# print("[ 프로그램 종료 ]")

num = 1
for _ in range(100000):
    if num==0:
        break
    num = int(input("숫자를 입력하세요(0 입력 : 종료) : "))
    print("입력한 값 : ",num)
print("[ 프로그램 종료 ]")
