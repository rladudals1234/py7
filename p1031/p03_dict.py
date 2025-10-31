# stu_list = [name:'홍길동',kor:100,eng:100,math:100,total:300,avg:100.0]
# stu_list = {키:값,키:값,키:값,키:값,키:값,키:값,...} # json과 유사하지만 다름

# stu_list = {'name':'홍길동','kor':100,'eng':100,'math':100,'total':300,'avg':100.0}
# print(stu_list)
# print(stu_list['name'])
# print(stu_list['kor'])
# print(stu_list['eng'])
# print(stu_list['math'])
# print(stu_list['total'])
# print(stu_list['avg'])

# 딕셔너리 생성
# list1 = [1,2,3]
# dic1 = {1:'a',2:'b',3:'c'}
# dic2 = {"no":1,"name":"홍길동","class":3}

# print(list1)
# print(dic1)
# print(dic2)
# print(dic2['no'])
# print(dic2['name'])
# print(dic2['class'])
# # 리스트 추가 - append,insert,extend
# # 딕셔너리 추가
# stu = {"학번":1,"이름":"홍길동","학과":"컴퓨터공학"}
# print(stu)
# stu["연락처"] = "010-1111-1111"
# print(stu)

# # 딕셔너리 수정
# stu["이름"] = "홍길자"
# print(stu)
# # print(stu['성명'])  # 없는 키를 출력할 때 에러
# stu['성명1'] = '홍'   # 없는 키는 딕셔너리 추가
# print(stu)

# # 딕셔너리 삭제
# del stu["학과"]
# print(stu)

# stu_list = [
#     {"no":1,"name":"홍길동","kor":100,"eng":100,"math":100,"total":300,"avg":100.0},
#     {"no":2,"name":"유관순","kor":90,"eng":80,"math":100,"total":270,"avg":90.0},
#     {"no":3,"name":"이순신","kor":100,"eng":100,"math":100,"total":300,"avg":100.0},
# ]

# print("번호:",stu_list[0]['no'])
# print("이름:",stu_list[0]['name'])
# print("국어:",stu_list[0]['kor'])
# print("영어:",stu_list[0]['eng'])    
# print("수학:",stu_list[0]['math'])
# print("합계:",stu_list[0]['total'])
# print("평균:",stu_list[0]['avg'])

a_dic = {"no":1,"name":"홍길동","kor":100,"eng":100,"math":100,"total":300,"avg":100.0}
# 국어점수를 출력하시오.
print("국어점수:",a_dic['kor'])
print(a_dic["kor"])        # 없는 키값 입력시 에러

# 딕셔너리 get()함수
print(a_dic.get("kor1"))     # 없는 키값 입력시 None타입으로 출력됨.

# 딕셔너리 keys()함수
print(a_dic.keys())         # 딕셔너리의 키값만 출력
a_list = list(a_dic.keys()) # 0번지 확인 위해 리스트 형식으로
print(a_list[0])    # 키의 0번지

# 딕셔너리 values()함수
print(a_dic.values())       # 딕셔너리의 값값만 출력
b_list = list(a_dic.values())
print(b_list)

# 딕셔너리 items()함수 - key, value
print(a_dic.items())        # 딕셔너리의 키와 값을 동시에 출력
c_list = list(a_dic.items())
print(c_list)

# items()함수와 2차원 리스트와 같다
aa_list=[
    ['no',1],
    ['name','홍길동'],
    ['kor',100],
    ['eng',100],
    ['math',100],
    ['total',300],
    ['avg',100.0]
]
# 홍길동을 출력하시오.
print("이름은", aa_list[1][1])

# 키 존재 확인
stu_dic = {"no":1,"name":"홍길동","kor":100,"eng":100,"math":100,"total":300,"avg":100.0}
if 'kor1' in stu_dic:
    print("키가 존재합니다.")
else:
    print("키가 존재하지 않습니다.")