# if문 :으로 닫아줘야함
# 아래문구는 들여쓰기로 닫아줘야함
if 1>5:    #괄호는 넣어도 되고 안 넣어도 됨
    print("정상입니다.")
else:
    print("비정상입니다.")  # 탭 또는 띄워쓰기중 한가지 방식으로 들여쓰기 반드시 필요(도커 리눅스환경에서 한가지로 하지 않으면 에러발생했었음)

# 숫자를 입력받아 100보다 큰수인지 아닌지 출력하시오.
# 100보다 큰수입니다. 100보다 작은수입니다.
num = int(input("숫자를 입력해주세요:"))
if(num>100):
    print("100보다 큰수입니다.")
else:
    print("100보다 작거나 같은수입니다.")

# 입력된 숫자가 짝수인지 홀수인지 출력하시오.
# 짝수입니다. 홀수입니다.
# num%2 == 0
# num = int(input("숫자를 입력해주세요:"))
if(num%2==0):
    print("짝수입니다.")
else:
    print("홀수입니다.")

# 내부모듈 - 외워두기
import datetime
now = datetime.datetime.now()
print(now)
print(now.year,"년도")
print(now.month,"월")
print(now.day,"일")
print(now.hour,"시")
print(now.minute,"분")
print(now.second,"초")

# 입력한 주민번호의 월을 파악해서 현재날짜와 같은 월이면
# 이벤트 대상입니다., 이벤트 대상이 아닙니다. 출력하시오.
n="03"
print(int(n))   #0이 제외된 3만 출력

# 991001-3111111
jumin = input("주민번호를 입력하세요:")
if(jumin[2:4]==str(now.month)):
    print("이벤트 대상입니다.")
else:
    print("이벤트 대상이 아닙니다.")
