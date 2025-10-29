# 로또번호 맞추기 프로그램
# 1. 변수선언, 로또번호 생성
import random
my_list = []    # 입력번호
c_list = []     # 맞춘번호
count = 0       # 맞춘개수
cnt = 0
lotto = random.sample(range(1,46),6)
lotto.sort()    # 로또정렬
# 2. 숫자입력
# 1~45사이의 숫자만 입력받기 - 유효성범위 벗어난 경우 카운트없이 재입력
while cnt < 6:
    num = int(input("로또 숫자를 입력하세요:"))
    if 0<num<46:
        if num in my_list:
            print("중복된 숫자입니다. 다시 입력하세요.")    # sample은 중복안되며 중복체크 필요없음
            cnt -= 1
        else:
            my_list.append(num)
    else:
        print("1~45사이의 숫자만 입력하세요.")
        cnt -= 1
    cnt += 1

# 유효성검사없이 6개 숫자 입력받기
# for i in range(6):
#     my_list.append(int(input("로또 숫자를 입력하세요:"))) # for문에 i값을 감소시켜 재입력 유도X

# 3. 당첨번호 확인
for i in lotto:
    for j in my_list:
        if i == j:
            c_list.append(j)
            count += 1
# 4. 결과화면 출력
print("[ 결과화면 ]")
print("-"*50)
print(lotto)
print(my_list)
print("맞춤번호 :",c_list)
print("정답개수 :",count)
# 5. 당첨금액 확인
if count == 6:
    print("당첨금 : 2,000,000,000원")
elif count == 5:
    print("당첨금 : 50,000,000원")
elif count == 4:
    print("당첨금 : 1,000,000원")
elif count == 3:
    print("당첨금 : 50,000원")
elif count == 2:
    print("당첨금 : 5,000원")
else:
    print("당첨금 : 0원")
