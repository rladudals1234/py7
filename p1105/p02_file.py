import os

# print("현재 작업 디렉터리:", os.getcwd())

# 1. 통로(stream) : 파일열기
# r:읽기모드, w:쓰기모드, a:추가모드
# f = open("c:/down/aaa.txt","r",encoding="utf-8")          # 절대경로
f = open("c:\\down\\aaa.txt","r",encoding="utf-8")          # 절대경로(역슬래쉬는 두번)
# f = open("./p1105/stuData.txt","r",encoding="utf-8")    # 상대경로(절대경로로 해도 됨 C:/workspace/p1105/stuData.txt)
# txt = f.read()      # 1byte씩 읽기(속도느림)
# txt = f.readline()  # 1줄씩 읽기(5줄이면 1줄만 읽음)
# txt = f.readlines() # 전체읽기(1줄씩 리스트)
# print(txt)

# readline() : 1줄씩 가져오기
# while True:
#     txt = f.readline()
#     if txt == "":
#         break
#     print(txt, end="")

# readlines() : 전체 가져오기
# txt_list = f.readlines() # 1줄씩 리스트에 담아서 가져옴
# for txt in txt_list:
#     print(txt, end="")

while True:
    txt = f.read()
    if txt == "":
        break
    print(txt, end="")

# 파일이름 또는 경로는 한글이 포함되지 않도록
f.close()
