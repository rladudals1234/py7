# from StuFunc import *       # StuFunc.py안에 모든 함수를 가져옴.
# 학생성적 프로그램
# while True:
#     screen_print() # 함수호출
#     choice = int(input("원하는 번호를 입력하세요.>> "))
#     if choice == 1:
#         # 학생성적입력
#         stu_input()
#         stu_print()     # 함수호출로 코드중복을 제거
#     elif choice == 2:
#         # 학생성적출력
#         stu_print()
#     elif choice == 3:
#         # 학생성적수정
#         stu_update()
#         stu_print()
#     elif choice == 4:
#         # 학생성적삭제
#         stu_delete()
#         stu_print()
#     elif choice == 0:
#         print("프로그램을 종료합니다.")
#         break

# 기본매개변수 - 호출함수(매개변수) 개수와 함수정의 매개변수 개수가 같아야 함.
# 가변매개변수 - 기본매개변수가 앞에오고, 뒤에 가변매개변수가 오면 매개변수 개수가
#              달라도 됨. 표기는 *매개변수 라고 하면 됨.(매개변수 위치가 제일 뒤여야 함)

# 키워드 매개변수 - 변수에 미리 값을 할당 b=10, b의 값이 들어오면 들어온 값 할당
#                b의 값이 없으면 기본 10할당
# 키워드 매개변수는 앞이 아닌 무조건 뒤에
def func(a,b=10):   # 키워드 매개변수 (2번째 매개변수에 b를 안 넣어도 default로 10으로 입력됨)
    print(a+b)
    
func(30)    # 30+10
func(30,20) # 30+20

# 가변매개변수
def func(a,*b):
    print(a)
    for i in b:
        print(i)

func(1,2,3,4,5,6,7,8,9,10)


def func(*a, b=10):
    print(b)
    for i in a:
        print(i)

func(1,2,3,4,5,6,7,8,9,10, b=5)
