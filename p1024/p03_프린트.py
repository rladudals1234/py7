# print() 다양한 출력
print(100)
print("합계")
print("-"*30)

print("100+100=",200)
print("299/3 =",(299/3))

# % print를 사용하면 소수점을 제어할 수 있음.
print("299/3=%.2f" % (299/3))

kor = 100   # 정수
eng = 100
math = 99
# %를 사용할 때 정수 : d, 실수 : f
# 100 + 100 + 99 = 299
print(kor,"+",eng,"+",math,"=",kor+eng+math)
print("%d + %d + %d = %d" % (kor,eng,math,(kor+eng+math)))

print("%d" % kor)   # %뒤에 있는 것을 출력
print("%5d" % kor)  # 5d : 5자리 공간을 확보해서 출력
print("%05d" % kor)  # 05d : 5자리 공간을 확보해서 빈공백은 0으로 채움
print("%010d" % kor)
print("%d" % 10000000000)
print("%2f" % 10.12345) # .2f : 소수점 2자리까지 출력
total = kor+eng+math
print("합계 : %d 평균 : %.2f" % (total, (total/3)))