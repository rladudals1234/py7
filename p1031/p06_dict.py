names = ['홍','홍','김','이','유','이','홍','김','강','홍']
a_list = [1,2,3,1,1,2,1,3,4,5]

# 1:4, 2:2, 3:2, 4:1, 5:1   각 글자 빈도수(중복 나온 횟수)
# 해당값이 있는지 확인, 리스트
# if 7 in a_list:
#     print("존재")
# else:
#     print("없음")

# 해당값이 있는지 확인, 딕셔너리 똑같음.
# a_list = {'1':1,'2':3,'3':4}
# if 7 in a_list:
#     print("존재")
# else:
#     print("없음")

# for 변수 in 범위:     #범위 - range,list,문자열,딕셔너리-keys,items,튜플
# a_dic = {}
# for i in a_list:
#     a_dic[i] = 0
# print(a_dic)

# 딕셔너리 추가 - 없는 키를 입력하면 추가됨
# 키 - 타입은 상관없음. str,int,float,bool

# a_dic = {}
# b_dic = {}
# 1:0, 2:0, 3:0 딕셔너리를 추가하시오.
# for i in a_list:
#     a_dic[i] = 0
# print(a_dic)
# 2 : 5 변경하시오.
# b_dic[2] = 5
# print(b_dic)

# '홍':100, '이':90, '유':80 딕셔너리에  추가하시오.
# '이':95 변경하시오.
# '유'를 삭제하시오.
# c_dic = {}
# # c_dic = {'홍':100,'이':90,'유':80}
# c_dic['홍'] = 100
# c_dic['이'] = 90
# c_dic['유'] = 80
# c_dic['이'] = 95
# del c_dic['유']
# print(c_dic)

# 반복
# names = ['홍','홍','김','이','유','이','홍','김','강','홍']
# a_list = [1,2,3,1,1,2,1,3,4,5]
# a_dic = {}
# for i in a_list:
#     if i not in a_dic:
#         a_dic[i] = 1
#     else:
#         a_dic[i] = a_dic[i] + 1
# print(a_dic)

names = ['홍','홍','김','이','유','이','홍','김','강','홍']
a_list = [1,2,3,1,1,2,1,3,4,5]
n_dic = {}
# '홍':4
# for i in names:
#     if i not in n_dic:
#         n_dic[i] = 1
#     else:
#         n_dic[i] = n_dic[i] + 1
# print(n_dic)

english = {
    '사랑':'love',
    '차':'car',
    '커피':'coffee',
    '전화':'phone',
    '컴퓨터':'computer',
    '이름':'name',
    '한국':'korea'
}

# 영어 맞추기 프로그램을 구현하시오.
# 사랑 ? love
count = 0   # 정답의 개수
while True:
    for k,v in english.items():
        # 정답입력
        print("{} 은(는) 영어로 뭘까요?".format(k))
        answer = input("입력>> ")
        if v == answer:
            print("띵동! 정답입니다.")
            count += 1
        else:
            print("오답 : ",v)
    print("총 {}개중 {}개 정답을 맞추셨습니다.".format(len(english),count))
    if len(english) == count:
        print("모든 정답을 맞추셔서 프로그램을 종료합니다.")
        break
    else:
        print("모든 정답을 맞출때까지 다시 진행합니다.")
        count = 0
