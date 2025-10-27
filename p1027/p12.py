import datetime
now = datetime.datetime.now()
# 주민번호를 입력받아, 나이를 출력하시오.
# 990101-1111111
jumin = input("주민번호를 입력하시오:")
# print("나이 : %d" % (125-int(jumin[0:2])))

# 000101-3111111
# 1900년대 -> 1,2 / 2000년대 -> 3,4
# 2025년 기준 print(2025-(1900+y_num))
year = now.year
a1 = jumin[7]       # a1타입 - 문자열
num = int(a1)       # 문자열 -> 정수타입변경
year1 = jumin[:2]   # 문자열
y_num = int(year1)  # 문자열 -> 정수타입변경
# 1900년대생인지, 2000년대생인지 확인하시오.
if(num==1 or num==2):
    print(year-(1900+y_num))
else:
    print(year-(2000+y_num))
