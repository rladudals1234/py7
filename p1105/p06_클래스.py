# 기본변수 - 1개 값을 저장 int,float,str,bool
# 복합변수 - 여러개의 값을 저장 list,dict,tuple,set
# 클래스 - 여러개의 변수, 여러개의 함수까지 저장    class

# 클래스 사용시 장점 - 변수,함수 함께저장, 변수에 접근하는 제한, 
# 한번에 여러개의 변수,여러개의 함수를 바로 사용가능
# 동일한 변수를 묶음
# def 함수명():
#     프로그램
# class 이름:   # 첫글자를 대문자(웬만하면)
#     프로그램

a = [12,30,20]
a[0] = 50
print(a)    # 막을 방법이 없음
# aa = int(input("시간을 입력하세요.>>"))
# if aa>24:
#     print("에러입니다.")
#     # 프로그램 종료
# a[0] = aa

class cal:
    __hour = 12    # 접근제한 private
    minute = 30
    second = 20
    def setHour(self,hour):
        if hour>23:     # 23:59:59 -> 00:00:00
            print("23보다 큰수는 입력을 할 수 없습니다.")
            return
        self.__hour = hour
    def getHour(self):
        return self.__hour
time = cal()
# print(time.__hour)    # 클래스의 변수에 직접접근제한
print(time.getHour())
print(time.minute)
print(time.second)
print(time.setHour(50))
print(time.getHour())

class Car:
    # color = "white"
    # speed = 0   # 전역변수(인스턴스변수)
    
    # Car()
    def __init__(self, color, speed):   # 객체선언
        self.color = color      # 파이썬에서는 없으면 생성
        self.speed = speed
    def upSpeed(self, num): # 지역변수(this.변수명 동일)
        self.speed += num
    def downSpeed(self, num):
        self.speed -= num
# 클래스를 사용하려면(변수를 호출하거나 변수에 값을 입력하려면), 무조건 객체선언해야함.
# 객체선언
# 참조변수명 = 클래스명()
c = Car("red",100)   # c라는 참조변수
# 값읽기 - 참조변수명.변수명
print(c.color)
# 값수정 - 참조변수명.변수명 = 값입력
c.color = "red"
print(c.color)
c2 = Car("blue",0)
c2.upSpeed(100)
print(c2.speed)
