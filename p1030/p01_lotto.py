# 로또 맞추기 프로그램을 구현하시오.
# 1. 변수선언
import random
lotto = []          # 로또번호
my_list = []        # 내가 입력한 번호
an_list = []        # 맞춘번호
# 2. 6개 번호생성
# 6개를 랜덤으로 추출
lotto = random.sample(range(1,46),6)
lotto.sort()
# 3. 6개 번호입력

# for i in range(6):
#     num = int(input("{}번째 로또번호를 입력하세요:".format(i+1)))
#     if 1 <= num <= 45:
#         my_list.append(num)
icnt = 0
while icnt < 6:
    num = input("{}번째 로또번호를 입력하세요:".format(icnt+1))
    if not num.isdigit():   # 숫자인지 확인
        print("숫자만 입력가능합니다.")
        continue
    num = int(num)
    if 1 <= num <= 45:
        if num not in my_list:
            my_list.append(num)
            icnt += 1
        else:
            print("중복된 번호입니다. 다시 입력하세요.")
    else:
        print("1~45사이의 번호 입력하세요.")
# 4. 번호확인
# lotto = [1,2,3,4,5,7]   # 테스트용
# for lo in lotto:
#     for my in my_list:
#         if lo == my:
#             an_list.append(my)
for my in my_list:
    if my in lotto:     # 랜덤로또전체를 가져와서 입력한 로또번호와 비교
        an_list.append(my)

# 5. 결과출력
print("로또번호:", lotto)
print("입력한 로또번호:", my_list)
print("맞춘번호:", an_list)
print("맞춘개수:", len(an_list))

# 6. 당첨금 출력
if len(an_list) == 6:
    print("당첨금 : 20,000,000원")
elif len(an_list) == 5:
    print("당첨금 : 50,000,000원")
elif len(an_list) == 4:
    print("당첨금 : 1,000,000원")
elif len(an_list) == 3:
    print("당첨금 : 50,000원")
elif len(an_list) == 2:
    print("당첨금 : 5,000원")
else:
    print("당첨금 : 0원")