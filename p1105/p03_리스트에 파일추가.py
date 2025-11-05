import os

#--------------------------------------------------------
# w : 쓰기모드
# f = open("./p1105/ccc.txt","w",encoding="utf-8")    # 파일없으면 w:모드는 파일을 생성
f = open("./p1105/ccc.txt","a",encoding="utf-8")    # a:모드는 기존 텍스트 마지막에 쓰기(이어서 게속 추가가능)
stu_data = ""
for i in range(3):
    txt = input("성적을 입력하시오.>> ")
    stu_data += txt+"\n"
f.write(stu_data)
# f.write("안녕하세요.\n반갑습니다.")
f.close()
print("파일 쓰기 완료")
#--------------------------------------------------------

# print('안녕하세요. "홍길동" 입니다.')
# print("안녕하세요. \"홍길동\" 입니다.")

# f = open("./p1105/stuData.txt","r",encoding="utf-8")
# txt = f.read()
# while True:
#     txt = f.read()
#     if txt == "":
#         break
#     print(txt.strip())  # 공백제거 (strip으로 쓰면 엔터키없음) -> 줄바꿈없이 하단코드와 비슷
#     # print(txt,end="")   # 안녕하세요 (엔터키)

# txt = f.readline()
# print(txt.strip())
# print(txt.strip().split(","))       # 리스트타입 - strip:공백제거, split()분리
# print(txt.strip().split(",")[5])    # 합계만 가져오기
# f.close()


# 3개를 출력하시오.
# 3개를 a_list 리스트 출력하시오.
# [['안녕', 'hello'],['사랑','love'],['감사','thank']]
f_bbb = open("./p1105/bbb.txt","r",encoding="utf-8")
a_list = []
while True:
    txt = f_bbb.readline()
    if txt == "":
        break
    a_list.append(txt.strip().split(","))
print(a_list)
f_bbb.close()

# 리스트안에 딕셔너리형태로 넣기
f = open("./p1105/stuData.txt","r",encoding="utf-8")
b_list = []
while True:
    txt = f.readline()
    if txt == "":
        break
    aa = txt.strip().split(",")
    b_list.append({"stuno":aa[0],"name":aa[1],"kor":aa[2],"eng":aa[3],"mat":aa[4],"tot":aa[5],"avg":aa[6],"rank":aa[7]})
for i in b_list:
    print(i)
f.close()