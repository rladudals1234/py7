import random

# 1,45까지 6개의 랜덤 숫자를 출력하시오.
# 중복은 안됨
# 1. 사용자가 6개의 숫자를 입력받아 리스트에 저장하시오.
my_list = []    # 입력번호
c_list = []     # 맞춘번호
count=0         # 맞춘개수
# 2. 로또번호 생성
lotto = random.sample(range(1,46),6)
lotto.sort()    # 로또정렬
# 3. 6개 숫자를 입력받아 출력하시오.
for i in range(6):
    my_list.append(int(input("로또 숫자를 입력하세요:")))
print("[ 결과화면 ]")
print("-"*50)
print(lotto)
print(my_list)

# 4. 당첨된 번호를 확인하고 싶은경우
for i in lotto:
    for j in my_list:
        if i == j:
            c_list.append(j)
            count += 1
print("맞춤번호 :",c_list)
print("정답개수 :",count)

# 정답개수 확인
# lotto = [5,9,24,36,44,45]
# my_list = [1,2,7,15,24,30,36]
# count=0
# for i in lotto:
#     for j in my_list:
#         if i == j:
#             count += 1
#             break
# print("정답개수 :",count)

# 5. 당첨금액 확인
# 0,1개 - 0원 2개 - 5천원 3개 - 5만원 4개 - 1백만원 5개 - 5천만원 6개 - 20억원
if count == 6:
    print("당첨금 : 20억원")
elif count == 5:
    print("당첨금 : 5천만원")
elif count == 4:
    print("당첨금 : 1백만원")
elif count == 3:
    print("당첨금 : 5만원")
elif count == 2:
    print("당첨금 : 5천원")
else:
    print("당첨금 : 0원")
