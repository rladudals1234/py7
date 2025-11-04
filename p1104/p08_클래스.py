from S_func import *
# stu_list
# stu_list = [
#     {'stuno':10101,'name':'홍길동','kor':80,'eng':80,'math':80,'total':240,'avg':80.00,'rank':0},
#     {'stuno':10102,'name':'유관순','kor':90,'eng':90,'math':90,'total':280,'avg':90.00,'rank':0},
#     {'stuno':10103,'name':'이순신','kor':100,'eng':100,'math':100,'total':300,'avg':100.00,'rank':0}
# ]

# s1 = Student()
# s1.stuno = 1
# s1.name = "홍길동"
# s1.kor = 100
# s1.eng = 90
# s1.math = 80
# s1.total = s1.sum()
# s1.avg = s1.avg()
stu_list = []
# stu_list.append({'stuno':s1.stuno,'name':s1.name,'kor':s1.kor,'eng':s1.eng,'math':s1.math,'total':s1.total,'avg':s1.avg,'rank':s1.rank})

# s1 = Student(10101,"홍길동",80,80,80)
# s2 = Student(10102,"유관순",90,90,90)
# s3 = Student(10103,"이순신",100,100,100)
# stu_list.append(s1)
# stu_list.append(s2)
# stu_list.append(s3)

# for stus in stu_list:
#     print(stus)
        
# 학생성적들 저장
students = Stuscore(Student(10101,"홍길동",80,80,80))   # 객체선언
students.add(Student(10102,"유관순",90,90,90))
students.add(Student(10103,"이순신",100,100,100))
students.print()
