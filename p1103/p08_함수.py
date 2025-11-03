# 매개변수 개수는 호출하는 변수의 개수와 동일
# 매개변수 타입도 호출하는 변수타입과 일치
# def add(a,b):
#     return a+b

# a = add(1,2)
# print(a)

# 가변매개변수(매개변수 개수가 틀려도 문제없음 - 여러개 가능)
# def add(a,b,*c):    # 변수 앞에 *를 붙이면 가변매개변수가 됨.
#     sum = a+b
#     for i in c: # c:여러개 가능.
#         sum += i
#     return sum

# # c는 리스트 타입으로 변경됨
# print(add(1,2,3,4,5,6,7,8,9,10))

# print(1,2,3)    #가변매개변수 사용할일은 많지 않음

# def print_str(a,b,*c):
#     print(a)
#     print(b)
#     for i in c:
#         print(i)
#     print()

# print_str("안녕","사과","홍길동","점수",100)

# print_str("안녕","사과")    # 최소 2개 이상 - 가변매개변수는 들어와도 되고 안 들어와도 됨

# 여러개를 입력받아, 함수를 사용해서 출력하시오.
def print_str(*c):
    for i in c:
        print(i)
# 5번 입력받아 모두 출력하시오.
# 0을 입력하면 모두 출력되도록 구성하시오.
# str1 = [0,0,0,0,0]
# for i in range(5):
#     # str1.append(input("숫자를 입력하시오>> "))
#     str1[i] = input("문자를 입력하시오>> ")

# print_str(*str1)

# 국어,영어,수학 점수를 입력받아, retrurn을 적용
def sum(kor,eng,math):
    total = kor+eng+math
    return total
stus = [1,'홍길동',100,90,80]
print_str(*stus)
# stus = [1,'홍길동',100,90,80]
# 함수를 제대로 구성해서 stus리스트를 아래와 같이 변경하시오.
# stus = [1,'홍길동',sum(100,90,80,270,90.00)]
# 함수를 꼭 사용할 것

def avg(kor,eng,math):
    total = kor+eng+math
    avg = total/3
    return avg

stus.append(sum(stus[2], stus[3], stus[4]))
print(stus)
# stus.append(sum)

stus.append(avg(stus[2], stus[3], stus[4]))
print(stus)
# stus.append(avg)