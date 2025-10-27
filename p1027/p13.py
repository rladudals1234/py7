# 990101-1111111
# 070101-4111111
# 1 - 남자, 2 - 여자
# 1,3 -> 남자 2,4는 여자
# 주민번호를 입력받아, 남자인지, 여자인지 출력하시오.
jumin = input("주민번호를 입력하세오:")
ju1 = int(jumin[7])
# 비교시 문자열보다 숫자가 빠름
if(ju1==1 or ju1==3):
    print("남자입니다.")
else:
    print("여자입니다.")

# 홀/짝으로 주민번호 구분
# if(ju1%2==0):
#     print("짝수이면 여자")
# else:
#     print("홀수이면 남자")

# 현재 월을 가져와서 생일이 맞으면 이벤트 대상자 그렇지 않으면 이벤트 대상자가 아닙니다.
import datetime
month = datetime.datetime.now().month
if(month==int(jumin[2:4])):
    print("이벤트 대상자입니다.")
else:
    print("이벤트 대상자가 아닙니다.")
