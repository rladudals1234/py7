import os
stu_list = [
    {'stuno':10101,'name':'홍길동','kor':80,'eng':80,'math':80,\
        'total':240,'avg':80.00,'rank':0},
    {'stuno':10102,'name':'유관순','kor':90,'eng':90,'math':90,\
        'total':270,'avg':90.00,'rank':0},
    {'stuno':10103,'name':'이순신','kor':100,'eng':100,'math':100,\
        'total':300,'avg':100.00,'rank':0},
]
titles = ['번호','이름','국어','영어','수학','합계','평균','등수']
stu_count = 10104

# for stu in stu_list:
#     print(f"{stu['stuno']}\t{stu['name']}\t{stu['kor']}\t\
# {stu['eng']}\t{stu['math']}\t{stu['total']}\t\
# {stu['avg']}\t{stu['rank']}")

# dict타입 -> 문자열로 변환
# stu_str = f"{stu_list[0]['stuno']},{stu_list[0]['name']},{stu_list[0]['kor']},\
# {stu_list[0]['eng']},{stu_list[0]['math']},{stu_list[0]['total']},\
# {stu_list[0]['avg']},{stu_list[0]['rank']}"
# print(stu_str)

# f = open("./p1105/stuData.txt","w",encoding="utf-8")
# f.write(stu_str)
# f.close()

f = open("./p1105/stuData.txt","w",encoding="utf-8")
for stu in stu_list:
    f.write(f"{stu['stuno']},{stu['name']},{stu['kor']},\
{stu['eng']},{stu['math']},{stu['total']},\
{stu['avg']},{stu['rank']}\n")
f.close()

# 학생성적입력
def add(stu_count):
    print("[ 학생성적입력 ]")
    name = input("{}번 학생이름을 입력하세요.>> ".format(stu_count))
    kor = int(input("국어점수를 입력하세요.>> "))
    eng = int(input("영어점수를 입력하세요.>> "))
    math = int(input("수학점수를 입력하세요.>> "))
    total = kor+eng+math
    avg = total/3
    # 영어,수학,합계,평균 추가하기
    stu_list.append({'stuno':stu_count,'name':name,'kor':kor,'eng':eng,'math':math,'total':total,'avg':avg,'rank':0})
    f = open("./p1105/stuData.txt","a",encoding="utf-8")
    f.write(f"{stu_count},{name},{kor},{eng},{math},{total},{avg:.1f},{0}\n")
    f.close()
    stu_count = stu_count + 1       # 학생번호1증가
    print("성적입력이 완료되었습니다.")
    print()

# 학생성적출력
def print_stu():
    print(" "*10,"[ 학생성적리스트 ]")
    print("-"*50)
    print("{}\t{}\t{}\t{}\t{}\t{}\t{}".format(*titles))
    print("-"*50)
    f = open("./p1105/stuData.txt","r",encoding="utf-8")
    for stus in stu_list:
        txt = f.readline()
        if txt == "":
            break
        stus1 = txt.strip().split(",")
        print(f"{stus1[0]}\t{stus1[1]}\t{stus1[2]}\t{stus1[3]}\t{stus1[4]}\t{stus1[5]}\t{stus1[6]:.2f}\t{stus1[7]}")
    f.close()

# print_stu()
add(stu_count)