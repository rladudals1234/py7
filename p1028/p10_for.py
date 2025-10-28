# for문을 2번 사용 - 중첩for문
# for i in range(2,10):
#     print("[ {} 단 ]".format(i),end=" ")
#     for j in range(1,10):
#         # print(i,"*",j,"=",(i*j))
#         print("{} X {} = {}".format(i,j,(i*j)),end=" ")
#     print()

# 2,4...짝수단
# for i in range(2,10,2):
#     print("[ {} 단 ]".format(i),end=" ")
#     for j in range(1,10):
#         # print(i,"*",j,"=",(i*j))
#         print("{} X {} = {}".format(i,j,(i*j)),end=" ")
#     print()

# 짝수단 if조건으로 continue사용
# for i in range(2,10,2):
#     if i%2 != 0:
#         continue    # 1번만 제외(9번 실행), break:완전중지
#     print("[ {} 단 ]".format(i),end=" ")
#     for j in range(1,10):
#         # print(i,"*",j,"=",(i*j))
#         print("{} X {} = {}".format(i,j,(i*j)),end=" ")
#     print()

# 중첩for문을 사용해서 00,01,02,03.....11,12,13....99
# for i in range(0,10):
#     for j in range(0,10):
#         print(f"{i}{j}")

# 중첩for문을 사용해서 000,001,002,003.....511,512,513....999
# for i in range(0,10):
#     for j in range(0,10):
#         for k in range(0,10):
#             print(f"kb국민 번호표 : {i}{j}{k}")

# 501~1000까지 홀수의 합을 출력하시오.
# sum=0
# for i in range(501,1001,2):
#     sum += i
#     print(i)
# print(sum)

# 1~100까지 3의 배수의 합을 출력하시오.
# sum=0
# for i in range(1,100):
#     if(i%3==0):
#         sum += i
#         print("3의 배수 :",i)
# print("3의 배수 총합 :",sum)

fruits = ['사과','배','복숭아','딸기','포도']
print("[ 과일리스트 ]")
for i,fruit in enumerate(fruits):   # enumerate() 함수 : index번호 리턴
    print(f"{i}.{fruit}")   # 1.사과 2.배 3.복숭아

print("[ 과일리스트 - range ]")
for i in range(len(fruits)):
    print(f"{i}.{fruits[i]}")
