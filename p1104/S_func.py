# 학생 1명의 성적을 저장하는 클래스
class Student:
    # stuno = 0
    # name = ""
    # kor = 0
    # eng = 0
    # math = 0
    # total = 0
    # avg = 0
    # rank = 0
    
    # 생성자
    def __init__(self, stuno, name, kor, eng, math):    # 생성자 - 객체선언시 함수호출
        self.stuno = stuno  # self 자동으로 변수 생성
        self.name = name
        self.kor = kor
        self.eng = eng
        self.math = math
        self.total = self.sum()
        self.avg = self.avg_f()
        self.rank = 0

    def sum(self):
        self.total = self.kor + self.eng + self.math
        return self.total
    
    def avg_f(self):
        self.avg = self.total / 3
        return self.avg

# 학생성적들을 저장하는 공간 클래스
class Stuscore:
    stu_list = []
    titles = ['번호','이름','국어','영어','수학','합계','평균','등수']
    def __init__(self,s):
        self.stu_list.append(
            {'stuno':s.stuno,'name':s.name,'kor':s.kor,'eng':s.eng,'math':s.math,'total':s.total,'avg':s.avg,'rank':s.rank}
        )
    
    # 학생성적 1명 추가함수
    def add(self,s):
        self.stu_list.append(
            {'stuno':s.stuno,'name':s.name,'kor':s.kor,'eng':s.eng,'math':s.math,'total':s.total,'avg':s.avg,'rank':s.rank}
        )
        print("학생이 추가되었습니다.")

    # 학생성적 출력함수
    def print(self):
        print(" "*10,"[ 학생성적리스트 ]")
        print("-"*60)
        print(*self.titles, sep="\t")
        print("-"*60)
        for stus in self.stu_list:
            # dict라서 stus['']
            print(f"{stus['stuno']}\t{stus['name']}\t{stus['kor']}\t{stus['eng']}\t\
{stus['math']}\t{stus['total']}\t{stus['avg']}\t{stus['rank']}")
        print()

    # 학생성적 정렬함수
    def rank(self):
        for s1 in self.stu_list:
            count = 1
            for s2 in self.stu_list:
                if s1['total'] < s2['total']:
                    count += 1
            s1['rank'] = count