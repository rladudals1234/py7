# 5*5의 2차원 형태 리스트를 생성[[],[],[],[],[]]
# a_list = [1,2,3,4,5,6,7,8,9]    #len(a_list) => 9
# b_list = [[1,2,3],[4,5,6],[7,8,9]]  #len(b_list) => 3

# b_list[1][0] = 100
# b_list[2][1] = 50
# print(b_list)

# 1차원 리스트 출력
# for a in a_list:
#     print(a, end="\t")
# for bs in b_list:
#     for b in bs:
#         print(b, end="\t")
#         if b % 3 == 0:
#             # print(bs, end="\t")
#             print()

stu_list = [
    ["홍길동", 100, 90, 80, 240, 80.00],
    ["유관순", 90, 90, 90, 280, 90.00],
    ["이순신", 100, 100, 100, 300, 100.00],
]
titles = ['이름', '국어', '영어', '수학', '합계', '평균']
while True:
    print("[ 학생성적수정 ]")
    print("0. 홍길동")
    print("1. 유관순")
    print("2. 이순신")
    print("3. 종료")
    print("-"*30)
    num = int(input("수정하려는 학생번호를 입력하세요. >> "))
    if num == 3:
        break
    print("1. 국어성적수정")
    print("2. 영어성적수정")
    print("3. 수학성적수정")
    print("-"*30)
    subjects = int(input("수정할 과목을 선택하세요. >> "))
    print("[ {} 학생 {}점수 수정  ]".format(titles[subjects],stu_list[num][0]))
    print("현재 {}점수 : {}".format(titles[subjects],stu_list[num][subjects]))
    score = int(input("수정할 {}점수를 입력하세요. >> ".format(titles[subjects])))
    stu_list[num][subjects] = score
    # 합계, 평균 변경
    stu_list[num][4] = stu_list[num][1] + stu_list[num][2] + stu_list[num][3]  # 합계변경
    stu_list[num][5] = stu_list[num][4] / 3  # 평균변경
    print(stu_list)

# 0. 홍길동
# 1. 유관순
# 2. 이순신
# --------
# 수정하고 싶은 학생의 번호를 입력하세요.
# 국어점수를 변경하는 프로그램을 구현하시오.
# print(\
#     '''
#     [ 수정할 학생번호 ]
#     0. 홍길동
#     1. 유관순
#     2. 이순신
#     '''
# )
# num = int(input("수정할 학생번호를 입력하세요. >> "))
# 1번 선택
# 국어점수를 70점으로 변경하고, 합계와 평균을 변경해서 출력하시오.
# stu_list[num][1] = 70
# stu_list[num][4] = stu_list[num][1] + stu_list[num][2] + stu_list[num][3]
# stu_list[num][5] = stu_list[num][4] / 3
# print(stu_list)

# while True:
#     num = int(input("수정할 학생번호를 입력하세요. >> "))
#     kor = int(input("수정할 국어점수를 입력하세요. >> "))
#     eng = int(input("수정할 영어점수를 입력하세요. >> "))
#     math = int(input("수정할 수학점수를 입력하세요. >> "))
#     stu_list[num][1] = kor
#     stu_list[num][2] = eng
#     stu_list[num][3] = math
#     stu_list[num][4] = stu_list[num][1] + stu_list[num][2] + stu_list[num][3]
#     stu_list[num][5] = stu_list[num][4] / 3
#     print(stu_list)

# stu_list[2][2] = 70
# stu_list[2][4] = stu_list[2][1] + stu_list[2][2] + stu_list[2][3]
# stu_list[2][5] = stu_list[2][4] / 3
# print(stu_list)

# print(stu_list[1][3])
# print(stu_list[2][0])
# stu_list[2][2] = 80
# print(stu_list)
