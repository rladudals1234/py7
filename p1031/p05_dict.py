# {키:값}
stu_dic = {"no":1,"name":"홍길동","kor":100}
# dict추가
stu_dic["eng"] = 90
# dict수정
stu_dic["kor"] = 10
# dict삭제
del stu_dic["name"]
print(stu_dic)
# keys() 출력
print(stu_dic.keys())
print(list(stu_dic.keys()))     # list형식으로 변환
for k in stu_dic.keys():
    print("{} : {}".format(k, stu_dic[k]))
# values() 출력
print(stu_dic.values())
print(list(stu_dic.values()))   # list형식으로 변환
for i, v in enumerate(stu_dic.values()):
    print("{} , {}".format(i,v))
# items() 출력 - k, v
print(stu_dic.items())
print(list(stu_dic.items()))     # list형식으로 변환
for k, v in stu_dic.items():
    print("{} : {}".format(k,v))
# 딕셔너리 출력
stu_dic['name'] = "홍길동"
print(stu_dic['no'])
print(stu_dic['name'])
print(stu_dic['kor'])
print(stu_dic['eng'])
# print(stu_dic['math'])  # 없는 Key로 출력시 에러
print(stu_dic.get('kor'))
print(stu_dic.get('math'))  # 없는 Key로 출력시 실행됨. - None 출력

# 딕셔너리 정렬
import operator
names ={"홍길동":100,"유관순":80,"이순신":90,"김구":99,"강감찬":95}
# reverse=True -> 역순정렬, reverse=False -> 순차정렬
# itemgetter(0):키, itemgetter(1):값
names2 = sorted(names.items(), key=operator.itemgetter(0), reverse=True)
print(names)
print(names2)

# 리스트 정렬
a_list = [1,5,9,4,3]
# sort() -> 해당리스트 자체를 정렬
# a_list.sort()
a_list.reverse()    # 1,5,9,4,3 -> 3,4,9,5,1순서가 변경
# sorted() -> 다른변수에 저장가능, 원본은 변경안됨.
# reverse=True -> 역순정렬
b_list = sorted(a_list)
print(a_list)
print(b_list)

# 리스트의 최대값 - max : 리스트에서 최대값 출력
print(max(a_list))
# 리스트의 최소값 - min : 리스트에서 최소값 출력
print(min(a_list))