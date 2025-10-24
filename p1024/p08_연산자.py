# 산술연산자
# +(더하기), -(빼기), *(곱하기), /(나누기)
# //(몫), %(나머지), **(제곱)

# print(10+20)
# print(10-20)
# print(10*20)
# print(10/20)
# print('-'*30)
# print(10/3)     #3.3333333
# print(10//3)    #3
# print(10%3)     #1
# print(10**3)    #10*10*10=1000
# print('-'*30)

# 두수를 입력받아 위의 연산을 출력하시오.
# +,-,*,/,//,%,**
# num1 = int(input("첫번째 숫자를 입력하세요:"))
# num2 = int(input("두번째 숫자를 입력하세요:"))
# print("더하기결과:",(num1+num2))
# print("빼기결과:",(num1-num2))
# print("곱하기결과:",(num1*num2))
# print("나누기결과:",(num1/num2))
# print("몫결과:",(num1//num2))
# print("나머지결과:",(num1%num2))
# print("제곱결과:",(num1**num2))

### 780원 동전으로 교환을 하려고 해요.
### 500, 100, 50, 10원 동전 몇개로 교환해야 할까요?
# 500-1개(몫) 100-2개(나머지의 몫) 50-1개(나머지의 몫) 10-3개(나머지의 몫)
# money1 = 780//500
# money2 = 780%500//100
# money3 = 780%500%100//50
# money4 = 780%500%100%50//10
# print("500원 동전:%d개" % money1)
# print("100원 동전:%d개" % money2)
# print("50원 동전:%d개" % money3)
# print("10원 동전:%d개" % money4)

# coin=100
# money1 = coin//500
# money2 = coin%500
# money3 = money2//100
# money4 = money2%100
# money5 = money4//50
# money6 = money4%50
# money7 = money6//10
# money8 = money6%10

# print("500원 동전:%d개" % money1)
# print("100원 동전:%d개" % money3)
# print("50원 동전:%d개" % money5)
# print("10원 동전:%d개" % money7)

# 50000원, 10000원, 5000원, 1000원 지폐 교환
# coin=1597000
# money1 = coin//50000
# money2 = coin%50000
# money3 = money2//10000
# money4 = money2%10000
# money5 = money4//5000
# money6 = money4%5000
# money7 = money6//1000
# money8 = money6%1000  #동전으로 교환

# print("50000원:%d장" % money1)
# print("10000원:%d장" % money3)
# print("5000원:%d장" % money5)
# print("1000원:%d장" % money7)


# 내가입력한 지폐나 동전 교환권 50000원, 10000원, 5000원, 1000원 교환
coin=int(input("금액을 입력하세요:"))
money1 = coin//50000
money2 = coin%50000
money3 = money2//10000
money4 = money2%10000
money5 = money4//5000
money6 = money4%5000
money7 = money6//1000
money8 = money6%1000
money9 = money8//500
money10 = money8%500
money11 = money10//100
money12 = money10%100
money13 = money12//50
money14 = money12%50
money15 = money14//10
money16 = money14%10

print("입력금액:",coin,"원")
print("50000원:%d장" % money1)
print("10000원:%d장" % money3)
print("5000원:%d장" % money5)
print("1000원:%d장" % money7)
print("500원:%d개" % money9)
print("100원:%d개" % money11)
print("50원:%d개" % money13)
print("10원:%d개" % money15)