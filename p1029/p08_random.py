import random
# 1~10사이에 있는 랜덤숫자 생성
n_list = []     # 저장할 공간
r_num = random.randrange(1,101)
for i in range(10):
    my_num = int(input("숫자를 입력하세요:"))
    n_list.append(my_num)   # 리스트에 추가
    if r_num == my_num:
        print("당첨되었습니다.")
        break
    elif r_num > my_num:
        print("더 큰수를 입력하세요.!!!!!")
    else:
        print("더 작은수를 입력하세요.!!!!!")
print("당첨번호 :",r_num)
print("입력번호 :",n_list)

# randrange() 1~10까지의 랜덤숫자를 3개를 출력하시오.
# print(random.randrange(1,11))
# print(random.randrange(1,11))
# print(random.randrange(1,11))

# print(random.sample([1,2,3,4,5,6,7,8,9,10],5))
# print(random.sample(range(1,11),5))
# print(list(range(1,11)))
