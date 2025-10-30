import random
# 5*5 리스트 출력
# 5*5 = 25
a_list = list(range(1,26))
random.shuffle(a_list)
print(a_list)

# 무한반복 실행
while True:
    # 리스트 화면 출력
    print("     [ 좌표맞추기 게임 ]")
    print("-"*50)
    for idx, a in enumerate(a_list):
        print(a, end="\t")
        if (idx+1) % 5 == 0:      # 0번지부터 시작되므로 +1
            print()               # 줄바꿈
    print("-"*50)
    num = int(input("원하는 번호를 입력하세요. >> "))
    print()
    # 번호비교
    for idx,a in enumerate(a_list):
        if num == a:
            a_list[idx] = "X"   # 원하는 번호에 X표시
            break
