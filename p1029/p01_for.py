# for 변수 in 범위:
# pass - 빈공백 : for, if 한줄이라도 코드가 없으면 에러가 나기에 pass
# break - 반복문을 종료
# continue - 1회 반복문 제외시켜줌.
# for idx in range(10):
#     pass    # 아무것도 일어나지 않음 - 빈공백
#     print("프로그램 종료")  # 10번 실행
#     break   # 이 시점에서 반복문을 종료

# for i in range(10):
#     if i%2==0:
#         print(i)
#         continue    # 1회만 제외

# print("[ 구구단 ]")
# for i in range(2,10):       # 8
#     for j in range(1,10):   # 9
#         print("숫자 : ", j)    # 1-72
#     print("-"*50)

# for i in range(2,10):       # 8
#     for j in range(1,10):   # 9
#         print(j)            # 72

# for i in range(2,10):   # 8 - 2,3,4,5,6,7,8,9
#     print(i)

# for i in range(8):   # 8 - 0,1,2,3,4,5,6,7
#     print(i)

# 5,21까지 출력하시오.
# for i in range(5,22):
#     print(i)

# 1,10까지 출력하시오.
# for i in range(1,11):
#     print(i)

# 0,9까지 출력하시오. 홀수만 출력하시오.
# for i in range(0,10): # 조건으로
#     if i%2 == 1:
#         print(i)
# for i in range(0,10): # 조건으로
#     if i%2 == 0:
#         continue
#     print(i)
# for i in range(1,10,2): # 증가값으로 홀수만 출력
#     print(i)

# 구구단을 출력하시오.
# for i in range(2,10):
#     if i%2==0: continue
#     print(f"[ {i} 단 ]")
#     for j in range(1,10):
#         print(f"{i} X {j} = {i*j}")

# for 변수 in 범위 -> range, list, 문자열, 딕셔너리, 튜플
# names = ['홍길동','유관순','이순신','김구','강감찬']
# for name in names:
#     print(name)     # 1.홍길동, 2.유관순.....

# for name in enumerate(names):   # index번호, 값을 리턴
#     print(name[0],name[1])

# for i,name in enumerate(names):   # index번호, 값을 리턴
#     print(f"{i+1}.{name}")

# n_list = [
#     [1,'홍길동'],[2,'유관순'],[3,'이순신']
# ]

# for ns in n_list:   # [[1,'홍길동'],[2,'유관순'],[3,'이순신']]
#     for n in ns:
#         print(n, end=" ")

a_list = []
# for문을 사용해서 0을 10개 들어가는 리스트를 만드시오.
# append 추가
for i in range(0):
    a_list.append(0)
print(a_list)

# 리스트 타입 변환
a_list = list('0'*10)
print(a_list)

# 리스트 내포
a_list = ['0' for i in range(10)]
print(a_list)

a_list = [2*i*i for i in range(1,10)]
print(a_list)
