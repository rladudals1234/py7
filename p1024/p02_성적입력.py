# 국어,영어,수학 점수를 입력받아 합계와 평균을 출력하시오.
kor = int(input("국어점수를 입력하세요:"))
eng = int(input("영어점수를 입력하세요:"))
math = int(input("수학점수를 입력하세요:"))
total = kor+eng+math
print("합계: ",total)
print("평균: ",total/3)
print("평균: %.2f" % (total/3))