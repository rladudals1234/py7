# a_list = [1,2,3,4,5,6,7,8,9]
# print(a_list)
# b_list = list(range(1,10))
# print(b_list)
# c_list = [i for i in range(1,10)]
# print(c_list)
# d_list = ['0','0','0','0','0','0','0','0','0']
# print(d_list)
# e_list = ['0'*9]
# print(e_list)
# f_list = ['0' for _ in range(9)]
# print(f_list)

a_list = list(range(1,10))
b_list = []
#[
    # [1,2,3],
    # [4,5,6],
    # [7,8,9]
#]
# 1 2 3
# 4 5 6
# 7 8 9
# print(a_list)

# 3*3 리스트형태로 출력하시오.
# for i in a_list:
#     print(i, end="\t")
#     if i % 3 == 0:
#         print()

# a_list = [
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ]
# [[1,2,3],[4,5,6],[7,8,9]] # 2차원
# 3*3 리스트형태로 출력하시오.
# for aa in a_list:   #[1,2,3]    [4,5,6]    [7,8,9]
#     for a in aa:
#         print(a, end="\t")
#     print()

# 4*4 리스트형태로 출력하시오.
# c_list = list(range(1,17))
# for i in c_list:
#     print(i, end="\t")
#     if i % 4 == 0:
#         print()

# 5*5 리스트형태로 출력하시오.
# d_list = list(range(1,26))
# for i in d_list:
#     print(i, end="\t")
#     if i % 5 == 0:
#         print()

# a_list = [9,1,2,5,6,8,3,4,7]
# 9 1 2
# 5 6 8
# 3 4 7
# for i, val in enumerate(a_list):
#     print(val, end="\t")
#     if (i+1) % 3 == 0:
#         print()

import random
a_list = list(range(1,17))
random.shuffle(a_list)
print(a_list)
### 4 * 4 리스트 형태로 출력하시오.
for i, val in enumerate(a_list):
    print(val, end="\t")
    if (i+1) % 4 == 0:
        print()
