# 로또 맞추기 프로그램
# 로또 1개를 자동번호 추출로 입력받아,
# 몇개가 맞는지 출력하시오.
import random
# print(random.random())
# 로또 번호
lotto = random.sample(range(1,46),6)
print(lotto)
count = 0

# 자동추출 6개 my번호
my_lottos = []
for i in range(5):
    my_lottos.append(random.sample(range(1,46),6))
print("-"*50)
print(" [ 나의 랜덤 로또 번호 ]")
# 입력한 my숫자 번호
for my_lotto in my_lottos:
    print(my_lotto)

counts = []
# 번호비교
def cal():
    # print(lotto, my_lottos)
    for my_lotto in my_lottos:  # 6개 묶음 로또번호
        count = 0
        for i in my_lotto:  # 1개묶음 로또번호
            if i in lotto:   # 1개 번호가 로또번호에 있는지 확인
                count += 1
        counts.append(count)

# 맞는 개수
print("-"*50)
cal()
print(" [ 로또번호 맞춘 개수 ]  ")
print(counts)
print("-"*50)