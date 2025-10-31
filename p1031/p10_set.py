# 세트 - 키만 있음. 키 중복불가
# 세트를 하면 중복이 제거됨.
set1 = {1,1,2,3,4,2,5,4,4,4,1}
print(set(set1))    # 중복제거
print(set1)

a_list = [1,2,3,1,1,5,6,7,3]
print(set(a_list))

names = ['홍길동','유관순','이순신','홍길동','유관순']
print(set(names))
# 다음에 다른곳에 사용할 때 변수저장
nset = set(names)
print(nset)
