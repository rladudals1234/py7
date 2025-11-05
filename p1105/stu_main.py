import os
# 문자열 -> 딕셔너리타입으로 변경명령어
import ast
# stu_list = [
#     {'stuno':10101,'name':'홍길동','kor':80,'eng':80,'math':80,\
#         'total':240,'avg':80.00,'rank':0},
#     {'stuno':10102,'name':'유관순','kor':90,'eng':90,'math':90,\
#         'total':270,'avg':90.00,'rank':0},
#     {'stuno':10103,'name':'이순신','kor':100,'eng':100,'math':100,\
#         'total':300,'avg':100.00,'rank':0},
# ]
titles = ['번호','이름','국어','영어','수학','합계','평균','등수']
stu_count = 10104
file_nm = "stuData.txt"

# 파일을 읽어오기
# 파일 -> dict타입으로 변경해서 리스트에 추가
stu_list = []
f = open(f"./p1105/{file_nm}","r",encoding="utf-8")
while True:
    txt = f.readline()
    if txt == "":
        break
    t_list = txt.strip().split(",")
    t_dic = {'stuno':t_list[0],'name':t_list[1],\
'kor':t_list[2],'eng':t_list[3],'math':t_list[4],\
'total':t_list[5],'avg':t_list[6],'rank':t_list[7]}
    # t_dic = ast.literal_eval(txt)
    stu_list.append(t_dic)
f.close()

# 파일 -> 리스트[딕셔너리타입] -> 파일
stu_str = ""
for i in range(len(stu_list)):
    stu_str += f"{stu_list[i]['stuno']},{stu_list[i]['name']},{stu_list[i]['kor']},\
{stu_list[i]['eng']},{stu_list[i]['math']},{stu_list[i]['total']},\
{stu_list[i]['avg']},{stu_list[i]['rank']}\n"
f = open(f"./p1105/{file_nm}","w",encoding="utf-8")
f.write(stu_str)
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
    f = open(f"./p1105/{file_nm}","a",encoding="utf-8")
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
    f = open(f"./p1105/{file_nm}","r",encoding="utf-8")
    while True:
        txt = f.readline()
        if txt == "":
            break
        t_list = txt.strip().split(",")
        print(f"{t_list[0]}\t{t_list[1]}\t{t_list[2]}\t{t_list[3]}\t{t_list[4]}\t{t_list[5]}\t{t_list[6]:.2f}\t{t_list[7]}")
    f.close()

# print_stu()
# add(stu_count)