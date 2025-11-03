import random
stu_list = [
    [10101,'홍길동',80,80,80,240,80.00],
    [10102,'유관순',90,90,90,280,90.00],
    [10103,'이순신',100,100,100,300,100.00]
]
stu_count = 10104   # 학생번호
titles = ['번호','이름', '국어', '영어', '수학', '합계', '평균']

def screen_print():
    print("-"*50)
    print("     [ 학생성적프로그램 ]")
    print("-"*50)
    print("1.학생성적입력")
    print("2.학생성적출력")
    print("3.학생성적수정")
    print("4.학생성적삭제")
    print("0.프로그램종료")
    print("-"*50)
 
def stu_input():
    # 단순변수가 선언되면 함수에서는 변수를 새롭게 생성
    global stu_count
    global stu_list
    global titles
    print("-"*50)
    print("     [ 학생성적입력 ]")
    print("-"*50)
    name = input("학생이름을 입력하세요.>> ")
    kor = int(input("국어점수를 입력하세요.>> "))
    eng = int(input("영어점수를 입력하세요.>> "))
    math = int(input("수학점수를 입력하세요.>> "))
    total = kor+eng+math
    stu_list.append([stu_count,name,kor,eng,math,total,total/3])
    stu_count += 1

def stu_print():
    global stu_count
    global stu_list
    global titles
    print("-"*50)
    print("     [ 학생성적출력 ]")
    print("-"*50)
    print("{}\t{}\t{}\t{}\t{}\t{}\t{}\t".format(*titles))
    print("-"*50)
    for i in stu_list:
        print("{}\t{}\t{}\t{}\t{}\t{}\t{:.2f}\t".format(*i))

def stu_update():
    global stu_count
    global stu_list
    global titles
    print("-"*50)
    print("     [ 학생성적수정 ]")
    print("-"*50)
    for idx,val in enumerate(stu_list):
        print("{}. {}".format(idx+1,val[1]))
    num = int(input("수정할 번호를 입력하세요.>> "))
    print("{}. {}".format(num,stu_list[num-1][1]))
    info = int(input("수정하실 학생정보가 맞습니까? (1.yes,2.no) >> "))
    if info == 1:
        name = input("수정할 이름을 입력하세요.>> ")
        # 반복문, titles를 이용해서 kor, eng, math부분 하나로 사용가능 'stu_list[num-1][] = ...'식으로
        kor = int(input("수정할 {}점수를 입력하세요.>> ".format(titles[2])))
        eng = int(input("수정할 영어점수를 입력하세요.>> "))
        math = int(input("수정할 수학점수를 입력하세요.>> "))
        total = kor+eng+math
        stu_list[num-1] = [stu_list[num-1][0],name,kor,eng,math,total,total/3]
        print("수정완료했습니다.")

def stu_delete():
    global stu_count
    global stu_list
    global titles
    print("-"*50)
    print("     [ 학생성적삭제 ]")
    print("-"*50)
    for idx,val in enumerate(stu_list):
        print("{}. {}".format(idx+1,val[1]))
    num = int(input("삭제할 번호를 입력하세요.>> "))
    del stu_list[num-1]
    print("삭제되었습니다.")

# global잘 안 쓰임, 매개변수로 다른 파일에서 넣어서 사용가능 return으로 갱신
# 나중에 class 객체생성 배울때 참조
