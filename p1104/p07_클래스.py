# 클래스
# 클래스 내 변수, 함수를 사용하려면, 무조건 객체선언을 해야 사용할 수 있음
# 객체선언 : 참조변수 = 클래스명
class Car:
    color = ""
    speed = 0
    
    # 생성자는 생략가능
    # def __init__(self,color="",speed=0):
    #     self.color = color
    #     self.speed = speed
    
    
    # 클래스내 함수 첫 매개변수로 self
    def upSpeed(self, num):
        # 함수내 변수를 선택(self는 객체안 변수 this.와 같음)
        self.speed += num
    
    def downSpeed(self, num):
        self.speed -= num

c1 = Car()  # 객체선언 - 변수, 함수 사용
# 사용방법 - 참조변수.변수명
# 함수 - 참조변수.함수명
c1.color = "red"
c1.speed = 0
# 사용방법 - 참조변수.변수명
# 함수 - 참조변수.함수명
print(c1.speed)
c1.upSpeed(10)  # 클래스 내 함수 호출 - 참조변수.함수명()
print(c1.speed)
c1.upSpeed(20)
print(c1.speed)
c1.speed = -100 # 이와 같이 속도는 양의정수만 나와야 하는데 마이너스 접근가능하게 되면 -값이 나온다.

# 속도 50으로 증가, 속도 30 감소, 속도 100
# 속도를 출력하시오.
# 색상 => 파랑으로 변경하시오.
car = Car()
car.color = "파랑"
car.speed = 0
car.upSpeed(50)
car.downSpeed(30)
car.upSpeed(100)
print("속도 : ",car.speed)
print("색상 : ",car.color)

# 1. 객체선언 후 변수값 지정
c1 = Car() # 객체선언
c1.color = "파랑"   # 객체선언 후 변수지정
c1.speed = 100      # 객체선언 후 변수지정
c1.upSpeed(100)
c1.downSpeed(50)
print("속도 : ",c1.speed)
print("색상 : ",c1.color)

# 위에 테스트는 주석처리하고 아래는 생성자를 통한 변수값 지정

class Car:
    color = ""
    speed = 0
    
    # 생성자는 생략가능
    ## 생성자 객체선언시 값을 바로 할당할 수 있도록 해줌
    def __init__(self,color,speed):
        self.color = color  # self.변수명 시 없으면 클래스에 변수 추가해 줌.
        self.speed = speed
        self.tire = 4   # 변수가 없으면 자동생성
    
    # 클래스내 함수 첫 매개변수로 self
    def upSpeed(self, num):
        # 함수내 변수를 선택(self는 객체안 변수 this.와 같음)
        self.speed += num
    
    def downSpeed(self, num):
        self.speed -= num

# 2. 생성자를 통해 변수값 지정 - 생성자를 사용해서 프로그램을 함.
c2 = Car("파랑",100)
print("색상 : ",c2.color)
print("속도 : ",c2.speed)

c2.door = 5 # 클래스에 변수가 없으면 클래스에 자동으로 추가됨.
print("타이어 : ",c2.tire)
print("도어 : ",c2.door)
# print(c2.test)  # 변수값 지정 안된건 안됨

