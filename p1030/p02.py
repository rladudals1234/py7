import random
# 3*3 리스트 출력
a_list = list(range(1,10))
print(a_list)

# 랜덤섞기
random.shuffle(a_list)
# 무한반복 실행
while True:
    print("[ 좌표 맞추기 게임 ]")
    print("-"*30)
    for idx,a in enumerate(a_list):        # 1,2,3,4,5,6,7,8,9
        print(a, end="\t")
        if (idx+1) % 3 == 0:      # 0번지부터 시작되므로 +1
            print()
    print("-"*30)
    num = int(input("원하는 번호를 입력하세요. >> "))

    # 원하는 번호에 X표시
    for idx,a in enumerate(a_list):
        if a == num:
            a_list[idx] = 'X'
            break
# --------------------------
# c_list [1,2,3]
# c_list[1] = 100