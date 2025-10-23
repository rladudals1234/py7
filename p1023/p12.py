# 국어점수, 영어점수, 수학점수를 입력받아 평균,합계를 출력하시오.
num1 = int(input("국어점수를 입력하세요: "))
num2 = int(input("영어점수를 입력하세요: "))
num3 = int(input("수학점수를 입력하세요: "))
print("합계:", num1+num2+num3)  #쉼표사용자를 사용하면 타입이 달라도 된다.
print("평균:", (num1+num2+num3)/3)