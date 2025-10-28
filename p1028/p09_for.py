# for 변수 in 범위:
# for i in [0,1,2,3,4,5,6,7,8,9]:
#     print(i)
# for i in [50,3,26,5,9]:
#     print(i)
# for i in range(5):  #[0,1,2,3,4]
#     print(i,end=" ")
#     print(i,end="\t")

# 1~100까지 합을 구하시오.
# sum = 0
# for i in range(1,101):
#     sum = sum + i
# print("합계 :",sum)

# 100을 넘는 위치는 얼마를 더할때 일까요?
# 1+2+3+4+5+6+7+8+9+10+11+12+13+14
# sum = 0
# for i in range(1,101):
#     sum = sum + i
#     print(i, sum)
#     if sum>100:
#         print("100을 넘는 위치는",i)
#         break
    # sum = sum + i                 # sum에 i증가를 먼저 처리하지 않는 경우
# print("합계 :",i,sum)
# print(f"{i-1} 번째 : {sum-i}")    # sum에 i증가를 먼저 처리하지 않는 경우

# 1*2*3*4*...*10 결과값 출력하시오.
# result = 1
result = 1
for i in range(1,11):
    result *= i
    print(i,result)
    if result>100:
        print("100을 넘는 위치는",i)
        break
print(f"{i} 번째 : {result}")
# print("10까지 곱한 결과 :",i,result)

result = 1
for i in range(1,11):
    if result>100:
        print("100을 넘는 위치는",i)
        break
    result *= i
    print(i,result)
print(f"{i-1} 번째 : {result/i}")
