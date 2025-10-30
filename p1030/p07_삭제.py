stu_list = [
    ["홍길동", 100, 90, 80, 240, 80.00],
    ["유관순", 90, 90, 90, 280, 90.00],
    ["이순신", 100, 100, 100, 300, 100.00],
]
titles = ['이름', '국어', '영어', '수학', '합계', '평균']

# 1. 홍길동 80
# 2. 유관순 90
# 3. 이순신 100

# stu_list파일을 가지고 이름을 출력을 하시오.

# 반복문 없이 출력
# print(stu_list[0][0])
# print(stu_list[1][0])
# print(stu_list[2][0])

# for문 1번
# for i in range(len(stu_list)):
#     print(stu_list[i][0])

# for문 2번
# for stus in stu_list:
#     for stu in stus:
#         if stu == stus[0]:
#             print(stu)

# 1. 홍길동
# 2. 유관순
# 3. 이순신
# stu_list파일을 가지고 이름을 출력을 하시오.
while True:
    print("[ 학생성적삭제 리스트 ]")
    for idx, stus in enumerate(stu_list):
        print("{}. {}".format(idx+1,stus[0]))
    print("-"*50)
    num = int(input("삭제하려는 번호를 입력하세요. >> "))   # 1->0
    del stu_list[num-1]
    print(stu_list)
