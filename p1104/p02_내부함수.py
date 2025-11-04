
# 내부함수 - 함수내에 함수
# def outFunc(a,b):
#     def inFunc(n1,n2):
#         return n1+n2
#     return inFunc(a,b)
# print(outFunc(10,20))

# def outFunc(a,b):
#     result = inFunc(a,b)
#     return result

# def inFunc(n1,n2):
#     return n1+n2

# print(outFunc(10,20))

# lambda() 함수 - 함수를 한줄로 간단히 만든 것
# 함수선언,함수정의
def add(a,b):
    return a+b

# 함수호출
print(add(10,20))

# 함수축약 lambda()
# def선언하는 것과 같음.
# lambda 매개변수 : 함수수식
# result: 함수명(값,값)
add = lambda a=10,b=20 : a+b
print(add())
result = lambda a,b : a+b
print(result(5,10))
# 간단한 한줄만(조건등도 넣을 수 있음) lambda
# 복잡한건 함수를 만드는게 좋음

def cal(a):
    if a>0:
        return a
    else:
        return 0
cal = lambda a:a**2
print(cal(10))

result = lambda a:a%2
print(result(3))

# 복잡한 함수는 기본함수를 사용해야 함.

# map함수
# 결과값리스트 = map(함수,리스트)
# 결과값리스트 - map타입 객체 -> list타입으로 변경
my_list = [1,2,3,4,5]
def cal(a):
    return a*10

# map(함수,리스트) -> 리스트안에 있는걸 각각 처리해줌(대량의 데이터 처리 속도)
m_list = list(map(cal,my_list))
print(m_list)
# def cal(a):
#     return a%2

m_list = list(map(lambda a:a%2,my_list))    # 이 상황에 주로 람다 사용됨
print(m_list)

# 람다식함수 - 함수축약 lambda(매개변수:수식)
# map함수 - 여러개를 함수적용시킬때 사용 / 리스트 = map(함수,리스트)
m_list = list(map(lambda a:"{}원".format(a*1425),my_list))    # 이 상황에 주로 람다 사용됨
print(m_list)
m_list = list(map(lambda a:a*10,my_list))
print(m_list)
my_list = [1,2,3,4,5]
m_list = list(map(lambda a:a+100,my_list))
print(m_list)
