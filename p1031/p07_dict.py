import random
english = {
    '사랑':'love',
    '차':'car',
    '커피':'coffee',
    '전화':'phone',
    '컴퓨터':'computer',
    '이름':'name',
    '한국':'korea',
    '상자':'box',
    '사과':'apple',
    '네트워크':'network',
    '피자':'pizza',
    '쇼핑':'shop',
    '햄버거':'hamburger',
    '미국':'america',
    '테이블':'table',
    '토마토':'tomato',
    '파스타':'pasta',
    '온라인':'online',
    '책':'book',
    '비행기':'airplane'
}

# 20문제중에 랜덤으로 5문제를 뽑아서 퀴즈를 만드시오.
# list = random.sample(list(english.keys()),5)
# c_list = []
# # 영어 맞추기 프로그램을 구현하시오.
# # 사랑 ? love
# count = 0   # 정답의 개수
# for i in list:
#     print("{} 은(는) 영어로 뭘까요?".format(i))
#     answer = input("입력>> ")
#     if english[i] == answer:
#         print("띵동! 정답입니다.")
#         count += 1
#         c_list.append({i:"정답, 입력:{}".format(answer)})
#     else:
#         print("오답 : ",english[i])
#         c_list.append({i:"오답, 정답:{}, 입력:{}".format(english[i],answer)})
# print("-"*50)
# print("총 {}개중 {}개 정답을 맞추셨습니다.".format(len(list),count))
# print("-"*50)
# for i in c_list:
#     print(i)

# 20문제중에 랜덤으로 5문제를 뽑아서 퀴즈를 만드시오.
a_list = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
quest = random.sample(a_list,5)     # 랜덤5개 - 20문제중 5개를 추출
quest.sort()                        # 랜덤5개를 순서대로 정렬
quest_dic = {}                      # 정답, 오답 입력을 위한 저장공간
num = 1
# print(quest)    #[0, 11, 12, 14, 17]
count = 0
for i,k in enumerate(english.keys()):   # index을 함계 추출,key
    if i in quest:
        # 정답입력
        print("{} 은(는) 영어로 뭘까요?".format(k))
        answer = input("입력>> ")
        # 정답확인
        if english[k] == answer:
            print("띵동! 정답입니다.")
            count += 1
            quest_dic[num] = "정답"   # i+1 = 1
        else:
            print("오답 : ",english[k])
            quest_dic[num] = "오답"
        num += 1
print("총 {}개중 {}개 정답을 맞추셨습니다.".format(len(quest),count))

# 1:정답 2:오답 3:오답 4:정답 5:정답
print(quest_dic)