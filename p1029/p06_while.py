n_list = []
cnt = 0
while True:
    if cnt < 4:
        name = input("{}번째 이름을 입력하세요:".format(len(n_list)+1))
        kor = int(input("{}번째 국어점수를 입력하세요:".format(len(n_list)+1)))
        eng = int(input("{}번째 영어점수를 입력하세요:".format(len(n_list)+1)))
        math = int(input("{}번째 수학점수를 입력하세요:".format(len(n_list)+1)))
        n_list.append([name,kor,eng,math])
        print(n_list)
    else:
        break
    cnt += 1

# 전체 출력
print(" [ 학생성적프로그램 ]    ")
print("-"*50)
print("이름\t국어\t영어\t수학")
print("-"*50)
for i in range(len(n_list)):
    print("{}\t{}\t{}\t{}".format(*n_list[i]))

# n_list = []
# n_list.append(1)
# n_list.append(2)
# n_list.append(3)
# n_list.insert(0,5)
# n_list.insert(2,100)
# n_list.extend([10,20,30])   # list타입을 추가
# n_list.append([100,200,300])
# n_list.append(['홍길동',100])
# print(n_list)

# while True:
#     name = input("이름을 입력하세요:")
#     n_list.append(name)
#     print(n_list)
#     print("-"*50)
#     print("이름\t국어\t영어\t수학\t합계\t평균")
#     print("-"*50)
#     print("{}".format(name))
