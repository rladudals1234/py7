# 일반변수 - 숫자(정수, 실수),문자열,불(True, False)
# 복합변수 - 리스트, 딕셔너리, 튜플, 세트 - 여러개 저장할 수 있음
# a=1
# b=2
# c=3
# 객체지향언어 : 클래스 - 변수, 함수 묶음
# 변수들, 함수들을 함께 묶음
# 이름,국어,영어,수학 - 평균을 구하는 함수, 합계함수

# 함수
# def 함수명()
#   프로그래밍

# 클래스 - 변수, 함수
# class 클래스명:
#   프로그래밍
# 클래스의 장점 : 
# 1. 변수,함수를 함께 묶음 2. 여러개 변수, 여러개 함수를 객체선언으로 동시 생성가능
# 3. 각각의 변수에 값을 제한할 수 있음 - 값제한, 접근제한
class Student:
    hour = 0
    minute = 0
    second = 0  # 변수 미리 지정
    
    # 생성자 - 함수를 호출하지 않아도, 객체선언시 자동호출
    def __init__(self, hour, minute, second):
        self.hour = hour
        self.minute = minute
        self.second = second

# s = Student # 객체선언
# s.hour=1    # hour 변수를 추가하는 방법
# s.minute=2  # 클래스 접근 : 참조변수.변수명 생성
# s.second=3  # 호출방법 : 참조변수.변수명 값 수정
 
# s2 = Student() # 객체선언
# s2.hour=1       # hour라는 변수를 추가하는 방법
# s2.minute=2     # 클래스 접근 : 참조변수
# s2.second=3

# 변수 읽어오기 : 참조변수.변수명 검색
# print(s2.hour)
# print(s2.minute)
# print(s2.second)

# 변수 = class명 : 객체선언 - class공간을 만들어줌.
s = Student(1,2,3)
print(s.hour)
print(s.minute)
print(s.second)
