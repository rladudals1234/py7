# 이름, 국어, 영어, 수학, 합계, 평균
stus = []
# 3명의 학생성적을 입력받아 stus에 모두 저장하여 출력하시오.

stu = []
stu.append(input("이름을 입력하세요:"))
stu.append(int(input("국어점수를 입력하세요:")))
stu.append(int(input("영어점수를 입력하세요:")))
stu.append(int(input("수학점수를 입력하세요:")))
total = stu[1]+stu[2]+stu[3]
avg = total/3
stu.append(total)
stu.append(avg)
#전체리스트에 추가
stus.append(stu)

stu = []
stu.append(input("이름을 입력하세요:"))
stu.append(int(input("국어점수를 입력하세요:")))
stu.append(int(input("영어점수를 입력하세요:")))
stu.append(int(input("수학점수를 입력하세요:")))
total = stu[1]+stu[2]+stu[3]
avg = total/3
stu.append(total)
stu.append(avg)
#전체리스트에 추가
stus.append(stu)

stu = []
stu.append(input("이름을 입력하세요:"))
stu.append(int(input("국어점수를 입력하세요:")))
stu.append(int(input("영어점수를 입력하세요:")))
stu.append(int(input("수학점수를 입력하세요:")))
total = stu[1]+stu[2]+stu[3]
avg = total/3
stu.append(total)
stu.append(avg)
#전체리스트에 추가
stus.append(stu)

print("성적리스트 : ",stus)