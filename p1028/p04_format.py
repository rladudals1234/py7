# year = 2025
# month = 10
# day = 28
# print("%d년 %03d월 %d일" % (year,month,day))
# day_format = "{:,d}년 {:03d}월 {}일".format(year,month,day)
# print(day_format)

# 3개의 값을 입력받아, 숫자를 모두 합친 금액을 출력하시오.
# 1000원 이상 입력하세요.
# 금액 : 1,000,000원
n1 = int(input("금액을 입력하세요:"))
n2 = int(input("금액을 입력하세요:"))
n3 = int(input("금액을 입력하세요:"))
total = n1+n2+n3
if(total >= 1000):
    print("1번금액 : {:,d}원 \n2번금액 : {:,d}원 \n\
        3번금액 : {:,d}원 \n총금액 : {:,d}원".format(n1,n2,n3,total))
else:
    print("1000원 이상 입력하세요.")

# 이름, 국어, 영어, 수학점수를 입력받아
# 홍길동, 국어, 영어, 수학, 합계, 평균 출력하시오.
# a_list = ['홍길동',100]
a_list = []
# 이름:홍길동, 국어:100
a_list.append(input("이름을 입력하세요:"))
a_list.append(int(input("국어점수를 입력하세요:")))
a_list.append(int(input("영어점수를 입력하세요:")))
a_list.append(int(input("수학점수를 입력하세요:")))
a_list.append(a_list[1]+a_list[2]+a_list[3])
a_list.append((a_list[1]+a_list[2]+a_list[3])/3)
print("이름:{} 국어:{} 영어:{} 합계:{} 평균:{:.2f}".format(*a_list))

a = 10
b = 20
print("1번째 값 : {},2번째 값 : {}".format(b,a))    # 거꾸로
print(f"1번째 값 : {b},2번째 값 : {a}")