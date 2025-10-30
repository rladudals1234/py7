import random
# a_list = [1,2,3,4,5]
# b_list = list(range(1, 6))
# c_list = [i for i in range(1, 6)]   # 리스트 내포
# print(a_list)
# print(b_list)
# print(c_list)

# append, insert, extend
# del, pop, remove, clear
# 수정 : a_list[index] = 값
# index : 해당위치값 리턴
# aa_list = [10,5,15,7,9]
# print(aa_list.index(15))    # 해당값의 위치 확인

# 1. 비교
# num = int(input("원하는 번호를 입력하세요. >> "))
# for idx,aa in enumerate(aa_list):
#     if aa == num:
#         aa_list[idx] = "X"
# print(aa_list)

# 2. 비교
# num = int(input("원하는 번호를 입력하세요. >> "))
# if num in aa_list:
#     aa_list[aa_list.index(num)] = "X"
# print(aa_list)

# 5*5의 2차원 형태 리스트를 생성[[],[],[],[],[]]
bb_list = []
bb_list = list(range(1, 26))
random.shuffle(bb_list)
# for i in range(5):
#     print(bb_list[i*5:(i+1)*5])
print([bb_list[i*5:(i+1)*5] for i in range(5)])

# 좌표만들기
num = int(input("원하는 번호를 입력하세요. >> "))
if num in bb_list:
    bb_list[bb_list.index(num)] = "X"


# bb_list = random.sample(range(1,26),25)
# while True:
#     print("     [ 좌표맞추기 게임 ]")
#     print("-"*50)
#     for idx,val in enumerate(bb_list):
#         print(val, end="\t")
#         if (idx+1) % 5 == 0:
#             print()
#     num = int(input("원하는 번호를 입력하세요. >> "))
#     if num in bb_list:
#         bb_list[bb_list.index(num)] = "X"
# print(bb_list)