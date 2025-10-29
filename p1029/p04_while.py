# 이름, 국어, 영어, 수학
# 입력받아, 출력하시오.
# 이름:홍길동 국어:100
# strs = ['이름', '국어', '영어', '수학', '합계', '평균']
# list = []
# cnt = 1
# list.append(input(f"{strs[0]}을 입력하세요:"))
# while cnt<len(strs)-2:    # while문 사용
#     list.append(int(input(f"{strs[cnt]}점수를 입력하세요:")))
#     cnt += 1
# total = sum(list[1:])
# list.append(total)
# list.append(total/3)
# for i,str in enumerate(strs):
#     print(f"{str}:{list[i]}", end=" ")

# ['홍길동',100,90,80,270,90.00]
# strs = ['이름', '국어', '영어', '수학', '합계', '평균']
# stu_list = []
# cnt = 1
# stu_list.append(input(f"{strs[0]}을 입력하세요:"))
# while cnt<len(strs)-2:    # while문 사용
#     stu_list.append(int(input(f"{strs[cnt]}점수를 입력하세요:")))
#     cnt += 1
# total = sum(stu_list[1:])
# stu_list.append(total)
# stu_list.append(total/3)
# print(stu_list)
# print("{}, {}, {}, {}, {}, {:.2f}".format(*stu_list))

strs = ['이름', '국어', '영어', '수학']
stu_list = [input(f"{strs[0]}을 입력하세요:")]
scores = [int(input(f"{subject} 점수를 입력하세요:")) for subject in strs[1:]]
total = sum(scores)
stu_list += scores + [total, total / len(scores)]
print(stu_list)