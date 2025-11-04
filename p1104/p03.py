# 함수규칙 - 반복제거, 유지보수 용이, 코드 관리 편의성
# def 함수명():
#   프로그램 구현
def cal(a):
    for i in range(10):
        print(a)

a = 10
# 100번 실행
# print(a)*100을 사용할지 함수를 사용할지
cal(a)
