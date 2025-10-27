# 변수 - 숫자(정수, 실수), 문자열, 불(True,False)
# 리스트, 튜플, 셋
# 리스트 - 배열:데이터를 여러개 저장하는 공간
# 변수는 1개의 값만 저장
a = 10
a = 5
print(a)
fruit = ["사과","배","복숭아","딸기","포도"]
print(fruit[0])
numbers = [1,2,3,4,5]
print(numbers)
print(numbers[0])
total = ["사과",1,2,True,1.25]
print(total)
stuscore = ['홍길동',100,100,100,300,100.0]
print(stuscore)
# 추가
stuscore.append(200)    # 뒤에 추가
print(stuscore)
# 삭제
stuscore.pop()          # 뒤에 삭제
print(stuscore)
stuscore.remove("홍길동")
print(stuscore)
# 해당 리스트값 삭제
stuscore.remove(100)
print(stuscore)
# del 해당 번호 삭제
del total[0]    #0번째 방(사과)
print(total)
#1번째방 값5를 추가
stuscore.insert(1,"1번")    # 특정번지에 추가
print(stuscore)
# 리스트데이터추가 - append, insert
# 리스트데이터삭제 - pop, remove, del