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
    print("[ 학생성적 프로그램 ]")
    print("1. 학생성적입력")
    print("2. 학생성적출력")
    print("3. 학생성적수정")
    print("0. 프로그램종료")
    print("-"*20)
    no = int(input("원하는 번호를 입력하세요:"))
    if no == 0:
        print("프로그램종료")
        break
    elif no == 1:
        # 학생성적입력
        print("[ 학생성적입력 ]")
        strs = ['이름', '국어', '영어', '수학']
        stu_list = [input(f"{strs[0]}을 입력하세요:")]
        scores = [int(input(f"{subject} 점수를 입력하세요:")) for subject in strs[1:]]
        total = sum(scores)
        stu_list += scores + [total, total / len(scores)]
        print(stu_list)
    elif no == 2:
        # 학생성적출력
        print("[ 학생성적출력 ]")
    elif no == 3:
        # 학생성적수정
        print("[ 학생성적수정 ]")
    print()
