# 조건문 - if문, switch(파이썬에서는 없음)
# 반복문 - 여러번 실행
# for문, while()

# [시작:끝-1(한단계앞):스탭(증가값)]
# range - 범위, range(10) 10번 반복
# range(시작, 끝-1(한단계앞), 스탭(증가값))
# for 변수 in 범위 - 문법
for i in range(10): # 0~(10-1)까지
    print(i)
for i in range(5):  #0~4까지 실행
    print("%d번째 안녕하세요" % i)
for _ in range(5):  #0~4까지 실행
    print("hello")

for i in range(3,6):    #3~5까지 실행
    print("%d번째" % i)

for i in range(3,11,2): #3~10까지 2씩 증가하며 실행
    print(i)
print("-"*50)
sum=0
for i in range(1,11):
    sum+=i
    # print(i, "번째 합계 :",sum)
    print(f"{i}번째 합계 : {sum}")
print("총 합계 : ",sum)

a_list = ["홍길동",100,90,80]
for a in a_list:    # a_list[0], a_list[1]... 들어감
    print(a)
# 2차원리스트 - for문 2번, 3차원리스트-for문 3번
print("-"*50)
name = "홍길동유관순이순신"
for i in name:
    print(i)

# range() 숫자를 입력하세요란 글자를 10번 출력
sum = 0
for i in range(10):
    num = int(input(f"{i+1}번째 숫자를 입력하세요:"))
    sum += num
print("합계 : ",sum)

test_list = []
for i in range(10):
    test_list.append(input(f"{i+1:02d}번 숫자를 입력하세요:"))
print(test_list)
