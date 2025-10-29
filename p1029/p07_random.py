import random   # 선언, random 클래스 가져와서 쓰겠다.
print(random.random())  # 0.0000000000 <= x <1.00000000000
print(random.randrange(1,11))   # 1~10사이의 숫자를 랜덤으로 가져온다.(정수)
print(random.randint(1,11))     # 1~10사이의 숫자를 랜덤으로 가져온다.(정수)
print(random.sample([1,2,3,4,5],2)) # 해당리스트에서 2개를 랜덤으로 가져옴 - 중복이 안됨
print(random.sample([1,2,3,4,5],4)) # 해당리스트에서 4개를 랜덤으로 가져옴 - 중복이 안됨
print(random.choices([1,2,3,4,5],k=4))    # 해당리스트에서 4개를 랜덤으로 가져옴 - 중복이 가능
print(random.shuffle([1,2,3,4,5]))  # 해당리스트 순서를 랜덤으로 조정
a_list=[1,2,3,4,5]
random.shuffle(a_list)
print(a_list)
