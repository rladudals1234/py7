# print("%d" % (100,200)) # 에러 %자리와 뒤개수가 맞아야 함.
# print("%d %d" % (100)) # 에러
print("%d %d" % (100,200))  # %자리와 뒤개수가 일치

# str1 = "이름"
# str2 = "국어"
# str3 = "영어"
# str4 = "수학"
# str5 = "합계"
# /tr6 = "평균"
# print(str1, str2, str3, str4)
# \t 탭키적용, \n 줄바꿈.
name = input("이름을 입력하세요:")
kor = int(input("국어점수를 입력하세요:"))
eng = int(input("영어점수를 입력하세요:"))
math = int(input("수학점수를 입력하세요:"))
total = kor+eng+math
avg = total/3
print("-"*50)
print("%s\t%s\t%s\t%s\t%s\t%s" % ("이름","국어","영어","수학", "합계", "평균"))
print("-"*50)
print("%s\t%d\t%d\t%d\t%d\t%.2f" % (name,kor,eng,math,total,avg))