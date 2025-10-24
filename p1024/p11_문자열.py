# 삼중따옴표는 있는 그대로 출력
print("""abcdefghijk
    lmnopqr
    stuvwxyz""")

# 문자열
str1 = "안녕"
str2 = '안녕'
print(str1)
print(str1,str2)                    # 문자열출력
# %출력 자리수지정, 빈공백에 0을 표시 %05d, 소수점제한 %.2f
# %s:문자열, %d:정수, %f:실수
print("%s -- %s" % (str1, str2))    # 문자열출력

print("안녕"*10)    #문자열 반복연산
print("-"*50)       #다른 언어에서는 대체로 곱하기 안됨
print("이름\t국어\t영어\t수학\t합계\t평균") # \n.줄바꿈
# 문자열 선택
name="안녕하세요"   #주소값 확인
print(name[0])
print(name[-5])
print(name[1])
print(name[2])
print(name[3])
print(name[4])

# 문자슬라이싱 - 안녕하세요
print(name[0:4])    # 0부터 4까지 출력
print(name[2:4])    # 2부터 4까지 출력
print(name[2:])     # 입력하지 않으면 마지막까지 출력
print(name[:3])     # 앞자리 입력하지 않으면 처음부터 출력

# 문자길이
print(len(name))    # 문자열의 길이 출력

#슬라이싱 - 스텝
print(name[::2])    # 2칸씩 띄워서 출력=안하요
print(name[::-1])    # 반대로 출력

# 응용문제 880101-2111111 주민번호
# 1 - 남자, 2 - 여자, 3 - 남자, 4 - 여자
jumin = "880101-2111111"
# 2만 출력하시오.
print(jumin[7])
# 이것도 뒤에서 7자리에 위치한 2출력
print(jumin[-7])

jumin = input("주민번호를 입력하세요:")
if(jumin[7]=="2"):
    print("여자입니다.")
elif(jumin[7]=="1"):
    print("남자입니다.")
elif(jumin[7]=="3"):
    print("남자입니다.")
elif(jumin[7]=="4"):
    print("여자입니다.")
else:
    print("주민번호로 남자인지 여자인지 확인하기 어렵습니다.")

# 짝수는 여자 홀수는 남자
if(int(jumin[7])%2==0):
    print("여자입니다.")
else:
    print("남자입니다.")

# 주민번호 1,2,3,4번은 내국인 5번, 6번, 7번, 8번은 외국인
# 정규식으로 표현가능
