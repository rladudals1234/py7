# 클래스선언
# __init__함수사용
class Student:
    def __init__(self, stuno, name, kor, eng, math):
        # 클래스 사용하는 전역변수 = 함수내에 사용하는 지역변수
        self.stuno = stuno
        self.name = name
        self.kor = kor
        self.eng = eng
        self.math = math
        self.total = kor + eng + math
        self.avg = self.total / 3
        self.rank = 0
    # 합계
    def total_f(self):
        self.total = self.kor + self.eng + self.math
        return self.total
    # 평균
    def avg_f(self):
        self.avg = self.total / 3
        return self.avg
# 매개변수 __init__함수 매개변수 개수와 맞아야함. 5개를 넘겨줘야함.
s = Student(10101, "홍길동", 80, 80, 80)
print("국어 :", s.kor)      # 80
print("합계 :", s.total)    # 240
s.kor = 100
print("국어 :", s.kor)      # 100
s.total_f()
s.avg_f()
print("합계 :", s.total)    # 300
print("평균 :", s.avg)      # 100
