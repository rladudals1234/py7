num1, num2 = 100, 200
num3 = 300
num4 = 400
num5 = 100

# 관계연산자
print(num1==num2)               # 100 == 200 False
print(num1==num5)               # 100 == 100 True
print("5 < 7 : ",5<7)           #True
print("5 == 5 : ",5==5)         #True
print("10 >= 5 : ",10>=5)       #True
print("10 != 10 : ",10!=10)     #False
print("5 != 10 : ",5!=10)       #True

# and, or 논리연산자
print("(100>50) and (100<200) : ",(100>50) and (100<200))   #둘다True이면 True(and)
print("(100>50) and (300<200) : ",(100>50) and (300<200))   #하나만True이면 False(and)
print("(100>50) or (100<200) : ",(100>50) or (100<200))   #둘다True이면 True(or)
print("(100>50) or (300<200) : ",(100>50) or (300<200))   #하나만True이면 True(or)
print("(100<50) or (300<200) : ",(100<50) or (300<200))   #둘다False이면 False(or)

# 국어점수가 50점이거나 영어점수가 50점이상인 사람을 출력하시오.(or사용)
# 국어점수가 50점이면서 영어점수도 50점이상인 사람을 출력하시오.(and사용)
