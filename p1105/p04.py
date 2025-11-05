import os
# r:읽기모드, w:쓰기모드, a:추가모드
#--------------------------------------------------------
# 현재위치에 존재하는 모든 파일을 출력
print(os.listdir("c:/down/"))  # c:/down/ 경로안 폴더안에 모든 파일을 보여줌
# 파일이 존재하는지 확인
# print(os.path.exists("c:/down/"+"aaa.txt"))
# if os.path.exists("./p1105/ccc.txt"):
#     print("파일이 존재")
# else:
#     print("파일이 없음")
# 
# fname = input("검색하려는 파일이름을 입력하세요.>> ")
# # os.listdir(fname)
# if os.path.exists("./p1105/"+fname):
#     print("파일이 존재")
# else:
#     print("파일이 없음")

#--------------------------------------------------------
# f = open("./p1105/ccc.txt","a",encoding="utf-8")    # a:모드는 기존 텍스트 마지막에 쓰기(이어서 게속 추가가능)
# for i in range(5):
#     f.write(f"안녕하세요. {i} \n")
# f.close()
#--------------------------------------------------------

#--------------------------------------------------------
# f = open("./p1105/aaa.txt","r",encoding="utf-8")
# while True:
#     txt = f.readline()
#     if txt == "":
#         break
#     print(txt.strip())
# f.close()
#--------------------------------------------------------

# with open() 파일입출력
# with open("./p1105/aaa.txt","r",encoding="utf-8") as f:
#     while True:
#         txt = f.readline()
#         if txt == "":
#             break
#         print(txt.strip())
# # f.close() 자동으로 적용되어 생략가능

# 파일복사 - 문자읽기:r, 문자쓰기:w / 파일읽기:rb, 파일쓰기:wb
f = open("./p1105/nct1.jpg","rb")
f2 = open("./p1105/aaa/nct1.jpg","wb")

while True:
    nctfile = f.read(1)  # 1byte씩 읽기 # read():파일읽기, # readline(),readlines():문자읽기
    if not nctfile:
        break
    f2.write(nctfile)
f.close()
f2.close()
print("파일복사 완료")
