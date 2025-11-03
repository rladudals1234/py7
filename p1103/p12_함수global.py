# 두수를 입력받아, 두수사이의 합을 출력하시오.
# 1,10 -> 55가 출력
# 10,1 -> 55가 출력

# 1~10까지 합을 구하시오.
# 파이썬 문법에서만 가능
# def sum(num1, num2):
#     if num1 > num2:
#         num1, num2 = num2, num1 # 앞의 숫자가 클 경우 자리교환 - 파이썬 문법에서만 가능
#     sum = 0
#     for i in range(num1, num2+1):
#         sum = sum + i
#     return sum

# def sum(n1, n2):
#     n3 = 0
#     if n1>n2:       # 다른 프로그램언어에서 사용
#         n3 = n1
#         n1 = n2
#         n2 = n3
#     sum = 0
#     for i in range(n1, n2+1):
#         sum = sum + i
#     return sum

# 1~10까지 합을 구하시오.
# def sum(n1, n2):
#     if n1 > n2:
#         return sum_for(n2,n1)
#     else:
#         return sum_for(n1,n2)

# def sum_for(n1, n2):
#     sum = 0
#     for i in range(n1, n2+1):
#         sum = sum + i
#     return sum

# print(sum(1,10))
# print(sum(10,1))

a = 10
a_list =[1,2,3]
def cal():
    global a    # 함수밖 a변수 사용하고 싶은경우 선언(global안 쓰면 새로 함수안에만 사용가능한 지역변수 a생성)
    # a = 100     # 지역변수 - 함수를 벗어나면 값이 사라짐.
    print("a:",a)   # 값만 가져오면 전역변수에 있는 값을 가져올 수 있음.
    # 변수는 먼저 선언되고 값을 조정할 수 있음.
    # a = 4       # 전역변수와 같은 이름을 가진 변수에 값을 할당하면 에러
    print("a_list:",a_list)
    
cal()   # a = 100
a = 1   # 함수호출 위에 있으면 가져올 수 있음
print(a)

# 단순변수, 일반변수일 경우
# 함수내에서 전역변수를 사용하는 것은 가능
# 함수내에서 전역변수의 값을 재할당은 불가
# 함수내에서 전역변수의 값을 재할당하려면 global 변수 선언을 해야 가능

# 복합변수일 경우
# 함수내에서 전역복합변수를 사용가능
# 함수내에서 전역복합변수값을 제할당 가능
# 단 튜플은 수정자체가 불가
