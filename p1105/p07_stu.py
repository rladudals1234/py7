class Student:
    # 파이썬은 자바랑 다르게 접근제어가 1개만 있음
    # 스프링 set,get만들거나 어노테이션 set,get처리 비슷
    __stuno = 0
    __name = ""
    __kor = 0
    __eng = 0
    __math = 0
    __total = 0
    __avg = 0
    __rank = 0
    # 객체,참조변수를 출력하면 함수실행을 시킴
    # def __str__(self):
    #     return (f"{self.getStuno()}\t{self.getName()}\t{self.getKor()}\t{self.getEng()}\t{self.getMath()}\t{self.getTotal()}\t{self.getAvg():.2f}\t{self.getRank()}")
    
    # 전역변수 만들어짐.(인스턴스)
    def __init__(self, stuno, name, kor, eng, math):
        self.setStuno(stuno)
        self.setName(name)
        self.setKor(kor)
        self.setEng(eng)
        self.setMath(math)
        self.setTotal(kor + eng + math)
        self.setAvg(self.getTotal() / 3)
        self.setRank(0)
    
    def setStuno(self, stuno): # private method
        self.__stuno = stuno
    def getStuno(self):
        return self.__stuno
    def setName(self, name):
        self.__name = name
    def getName(self):
        return self.__name
    def setKor(self, kor):
        self.__kor = kor
    def getKor(self):
        return self.__kor
    def setEng(self, eng):
        self.__eng = eng
    def getEng(self):
        return self.__eng
    def setMath(self, math):
        self.__math = math
    def getMath(self):
        return self.__math
    def setTotal(self, total):
        self.__total = total
    def getTotal(self):
        return self.__total
    def setAvg(self, avg):
        self.__avg = avg
    def getAvg(self):
        return self.__avg
    def setRank(self, rank):
        self.__rank = rank
    def getRank(self):
        return self.__rank
    
    def s_total(self):
        self.setTotal(self.kor + self.eng + self.math)
        return self.getTotal()

    def s_avg(self):
        self.setAvg(self.getTotal() / 3)
        return self.getAvg()
    
    # def s_print(self):
    #     return (f"{self.getStuno()} {self.getName()} {self.getKor()} {self.getEng()} {self.getMath()} {self.getTotal()} {self.getAvg():.2f} {self.getRank()}")

class Students:
    stu_list = []
    titles = ['번호','이름','국어','영어','수학','합계','평균','등수']
    # def __init__(self,Student):
    #     self.stu_list.append(Student)
    
    def screen_print():
        print("-"*60)
        print(" "*10,"[ 학생성적프로그램 ]")
        print("-"*60)
        print("1. 학생성적입력")
        print("2. 학생성적출력")
        print("3. 학생성적수정")
        print("4. 학생성적삭제")
        print("5. 등수처리")
        print("0. 프로그램종료")
        print("-"*60)
    
    def add(self,Student):
        self.stu_list.append(Student)
    def print(self):
        print(" "*10,"[ 학생성적리스트 ]")
        print("-"*60)
        print(*self.titles, sep="\t")
        print("-"*60)
        for stu in self.stu_list:
            print(f"{stu.getStuno()}\t{stu.getName()}\t{stu.getKor()}\t{stu.getEng()}\t{stu.getMath()}\t{stu.getTotal()}\t{stu.getAvg():.2f}\t{stu.getRank()}")
        print()

    def stu_rank(self):
        for s1 in self.stu_list:
            count = 1
            for s2 in self.stu_list:
                if s1.getTotal() < s2.getTotal():
                    count += 1
            s1.setRank(count)
        print("등수처리가 완료되었습니다.")
        print()
            
# Students 클래스에서 리스트에 추가
stus = Students()
stus.add(Student(10101,"홍길동",100,100,99))
stus.add(Student(10102,"유관순",90,90,99))
stus.add(Student(10103,"이순신",80,80,99))
stus.stu_rank()
stus.print()

# s1 = Student(10101,"홍길동",100,100,99)
# print(s1)   # __str__() 쉽게 출력 (원래 객체 주소값으로 보임)
