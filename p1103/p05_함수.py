def cal(a,b):
    print("[ 사칙연산 ]")
    print(a+b)
    print(a-b)
    print(a*b)
    print(a/b)

# 두수를 입력해서 사칙연산을 하시오. 함수를 사용할것
# a = 10
# b = 2
# cal(a,b)
# -------------------------------------
# i = 0
# a_list = [0,0]
# while(True):
#     a = input("숫자를 입력하시오:")
#     if a.isdigit(): # 숫자인지 확인
#         a_list[i] = int(a)  # 타입변환
#         i += 1      # 1증가
#     else:
#         print("숫자만 입력가능합니다.!!")
#     if i ==2:
#         break
# cal(a_list[0],a_list[1])
# 무한반복되도록 하시오.
# 0을 입력하면 프로그램을 종료하시오.
while True:
    a = int(input("숫자를 입력하시오>> "))
    b = int(input("숫자를 입력하시오>> "))
    if a == 0 and b == 0:
        print("프로그램을 종료합니다.!!")
        break
    cal(a,b)
