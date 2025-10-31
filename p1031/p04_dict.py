stu_dic = {}
# "no":1,"name":"홍길동","kor":100,"eng":100,"math":100,"total":300,"avg":100.0
# 딕셔너리에 추가해서 키 : 값으로 모두 출력
# stu_dic['no'] = 1
# stu_dic['name'] = "홍길동"
# stu_dic['kor'] = 100
# stu_dic['eng'] = 100
# stu_dic['math'] = 100
# stu_dic['total'] = stu_dic['kor'] + stu_dic['eng'] + stu_dic['math']
# stu_dic['avg'] = stu_dic['total'] / 3
# print(stu_dic)

# for k, v in stu_dic.items():
#     print("{} : {}".format(k,v))

# for k in stu_dic.keys():
#     print("{} : {}".format(k,stu_dic[k]))   # 'no', stu_dic['no']

# for v in stu_dic.values():
#     print("값 : {}".format(v))

stu_list = [
    {"no":1,"name":"홍길동","kor":100},
    {"no":2,"name":"유관순","kor":80},
    {"no":3,"name":"이순신","kor":90}
]
# 3번째에 있는 kor -> 50으로 변경
stu_list[2]['kor'] = 50
print("3번째 사용자 국어점수:",stu_list[2]['kor'])
# kor -> 50으로 변경하시오.
stus = {"no":3,"name":"이순신","kor":90}
stus['kor'] = 50
print(stus)

a_list=[3,'이순신',90]
# 90 -> 50으로 변경하시오.
a_list[2] = 50
print(a_list)

