# 문자열 함수
# upper() - 대문자로 변경
# lower() - 소문자로 변경
# swapcase() - 대문자는 소문자로, 소문자는 대문자로 변경
# title() - 첫글자를 대문자로 변경

# 문자열 찾기
# count() - 해당되는 문자 개수
# find() - 해당 문자 위치 검색 - 없을때 -1리턴
# index() - 해당 문자 위치 검색 - 없을때 에러
# startswith() - 해당문자로 시작되는지 확인 True,False
# endswith() - 해당문자로 끝나는지 확인 True,False

# 공백제거
# strip() - 좌우 공백제거, 문자 사이 공백은 제거되지 않음.
# rstrip() - 오른쪽 공백제거
# lstrip() - 왼쪽 공백제거

# replace(변경전문자,변경후문자) - 문자열 변경

# split() - 문자열 분리 : 타입은 리스트로 분리 해줌.
# a_list = a.split(",")

# join() - 문자열 결합
# ss = "-"
# print(ss.join('파이썬'))


# map() : 리스트를 입력받아 처리하는 함수
# map(function함수부분,리스트데이터)

# isdigit() : 숫자인지 확인
# isalpha() : 문자(영문자,한글) 확인
# isalnum() : 문자(영문자,한글),숫자인지 확인
# islower() : 소문자 확인
# isupper() : 대문자 확인

# 국어점수를 입력하세요.
while True:
    kor = input('국어점수를 입력하세요.')
    if kor.isdigit(): # 숫자인지 확인
        break
    else:
        print("숫자가 아닙니다. 다시 입력하세요. ")    

print("숫자로 변경 : ",int(kor))



# def multi(x):
#     return x*2

# a = [1,2,3]
# b = list( map(multi,a) )
# print(a)
# print(b)



# a = ['100','90','80']
# print(map(int,a))
# b = list(   map(int,a)   )   # map타입객체로 저장
# print(a)
# print(b)




# a = ['100','90','80']
# b = []
# for i in a:
#     b.append(int(i))
    
# print(a)
# print(b)    



# a = '1,홍길동,100,100,100,300,100.0'
# titles = ['번호','이름','국어','영어','수학','합계','평균']

# # print(sep:변수사이사이 모두 적용, end:마지막에 한번적용)
# print(*titles,sep="/",end='**') # sep 사이 간격출력


# a_list = a.split(",")

# print(*titles,sep='\t') # sep 사이 간격출력
# print("-"*50)
# print(*a_list,sep='\t')

# a_list = a.split(',')
# print(int(a_list[2]))
# b = '홍길동 유관순 이순신 김구'
# b_list = b.split(' ')
# print(b_list[1])





# a = "홍길동은 키가 180, 홍길동은 몸무게 70, 홍길동은 사는 곳이 서울입니다."
# print(a.replace('홍길동','홍길자'))

# ' ',''
# a = "   a   b   c   "
# print(a.replace(' ','') ) 
# print(a.strip()) 

# input1 = input("이름을 입력하세요.>>  ").replace(' ','')
# if '홍길동' == input1:
#     print("맞습니다.",input1)
# else:
#     print('틀립니다.',input1)    




# a = '112233333445'
# print(a.count('3'))  # 3 - 5개 존재

# b = '프로그램 중 파이썬 사용자가 제일 많습니다.(파이썬 프로그래밍)'
# print(b.find('파이선')) # 왼쪽에서 검색, 파이썬 위치 검색 - 없을때 -1리턴
# print(b.rfind('파이썬')) # 오른쪽에서 검색
# print(b.index('파이썬')) # 파이썬 위치 검색, 없을때 에러
# print(b.startswith('파이썬'))
# c= "abc.xls"
# print(c.endswith("xls"))

# a = 'abc'
# # 대문자로 변경
# print(a.upper())

# b = 'aBBccDf'
# print(b.upper())


# # 문자열
# # 문자열 슬라이싱
# a = '안녕하세요'
# # 하세 출력하시오.
# print(a[2:4])
# print('안녕'*3)  # 3번반복
# print('안녕'+'hello') # 연결연산자