# 클래스선언
# __init__함수사용안하고(생성자 사용안하고)
class Student:
    # 합계
    def total_f(self):
        self.total = self.kor + self.eng + self.math
        return self.total
    # 평균
    def avg_f(self):
        self.avg = self.total / 3
        return self.avg

s = Student()
s.stuno = 10101
s.name = "홍길동"
s.kor = 80
s.eng = 80
s.math = 80
print("국어 :", s.kor)      # 100
s.total_f()
s.avg_f()
print("합계 :", s.total)    # 300
print("평균 :", s.avg)      # 100

class Student:
    def __init__(self, stuno, name, kor, eng, math):
        self.stuno = stuno
        self.name = name
        self.kor = kor
        self.eng = eng
        self.math = math
        self.total = self.total_f()
        self.avg = self.avg_f()
        self.rank = 0
    # 합계
    def total_f(self):
        self.total = self.kor + self.eng + self.math
        return self.total
    # 평균
    def avg_f(self):
        self.avg = self.total / 3
        return self.avg
class Stuscore:
    stu_list = []
    def __init__(self, s):
        self.stu_list.append(
            {'stuno':s.stuno,'name':s.name,'kor':s.kor,'eng':s.eng,'math':s.math,'total':s.total,'avg':s.avg,'rank':s.rank}
        )
        self.rank_f()
    def add(self,s):
        self.stu_list.append(
            {'stuno':s.stuno,'name':s.name,'kor':s.kor,'eng':s.eng,'math':s.math,'total':s.total,'avg':s.avg,'rank':s.rank}
        )
        self.rank_f()
    def print(self):
        for stus in self.stu_list:
            print(stus, sep="\t")
    
    def rank_f(self):
        for i in self.stu_list:
            i['rank'] = 1
            for j in self.stu_list:
                if i['total'] < j['total']:
                    i['rank'] += 1
        # return self.stu_list
s = Stuscore(Student(10101,'홍길동',80,80,80))
s.add(Student(10102,'유관순',90,90,90))
s.add(Student(10103,'이순신',100,100,100))
# s.rank_f()
s.print()
