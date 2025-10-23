# 변수 - 파일을 저장하는 공간
num = None
print(type(num))
num = 100
print(type(num))
# 타입 - 숫자(정수, 실수),문자열,불(True,False)
# 문자열 + 숫자 : 불가능

astr = 100
astr = True
astr = "안녕"   # 마지막값이 타입으로 지정됨
print(type(astr))

result = 100
result2 = result
result = result + 200
print(result2)  #값은 얼마일까요?
