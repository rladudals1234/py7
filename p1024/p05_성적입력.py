# 이름 입력(str), 국어점수 입력(int), 영어점수 입력(int), 수학점수 입력(int)하여 합계(int)와 평균(float)을 구하시오.
# 단 % print로 출력
name = input("이름을 입력하세요:")
kor = int(input("국어점수를 입력하세요:"))
eng = int(input("영어점수를 입력하세요:"))
math = int(input("수학점수를 입력하세요:"))
total = kor+eng+math
avg = total/3   # 실수

print("%s\t%d\t%d\t%d\t%d\t%.2f" % (name, kor, eng, math, total, avg))