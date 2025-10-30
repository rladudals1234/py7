# 1~10까지 합을 구하시오
# for문으로
# sum = 0
# for i in range(1,11):   #자동증감이 됨.
#     sum+=i
# print(sum)

# while문으로
# icount = 1
# sum = 0
# while icount <= 10:
#     sum += icount
#     icount += 1    # 증감식 - 추가
# print(sum)

# 5번 동안 숫자를 입력받아 합계를 출력하시오.
# for문, while문
# sum = 0
# for i in range(5):
#     sum += int(input("숫자를 입력하세요:"))
# print(sum)

# sum = 0
# cnt = 0
# while cnt<5:
#     sum += int(input("숫자를 입력하세요:"))
#     cnt += 1
# print(sum)

# while
stu_list = []
while True:
    print("[ 학생성적프로그램 ]")
    print("1. 학생성적입력")
    print("2. 학생성적출력")
    print("3. 학생성적수정")
    print("0. 프로그램종료")
    print("-"*20)
    choice = int(input("원하는 번호를 입력하세요."))
    # choice == 0 비교
    if choice==0:
        break
    elif choice==1:
        # 학생성적입력
        print("[ 학생성적입력 ]")
        name = input("이름을 입력하세요.")
        kor = int(input("국어점수를 입력하세요. "))
        eng = int(input("영어점수를 입력하세요. "))
        math = int(input("수학점수를 입력하세요. "))
        total = kor+eng+math
        avg = total/3
        stu_list.append([name,kor,eng,math,total,avg])

        print("이름\t국어\t영어\t수학\t합계\t평균\t")
        print("-"*50)
        # [ 
        #    ['홍길동',kor,eng,math,total,avg],
        #    ['유관순',kor,eng,math,total,avg]
        # ]
        print("{}\t{}\t{}\t{}\t{}\t{:.2f}\t".format(name,kor,eng,math,total,avg))
    print()

# while 종료후
print(stu_list)
