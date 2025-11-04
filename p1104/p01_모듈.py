# 모듈 : 함수의 집합
# 다른 파일의 모듈을 사용하려면, import을 해야 사용가능
# improt를 하면 이름.함수명으로 호출해야 함.
# from ..p1103.StuFunc import * # 상위에서 실행해야 됨
# import p1103.StuFunc as StuFunc
# print(random.randint(1,10))
# StuFunc.screen_print()

# import Func.func1   # 이름.함수명으로 호출해야 함.
import Func
print(Func.func1())
print(Func.func2())

# from 파일명 import 함수를 정의하면 파일명을 생략가능
# 모듈명을 생략가능
# from 모듈명 import 변수, 함수, 클래스
# 덧셈,뺄셈,곱셈,나눗셈 한 그룹에 묶어두면 -> 유사한 그룹으로 묶어서 사용하면 편함
from Func import func1, func2, stu
print(func1())  # 함수사용
print(func2())
s1 = stu()  # 클래스 사용

# 예제
# 수학공식
from math import sin,cos,tan,floor,ceil
# floor 소수점 버림, ceil 소수점 올림, round 반올림(math모듈 아님)
print(floor(1.95))
print(ceil(1.2))
print(round(1.59))  # round 내장함수

print(sin(3.14))
print(cos(3.14))
print(tan(3.14))
print(floor(3.14))
print(ceil(3.14))
print(round(3.14))

# 모듈이름이 너무길때 줄여 사용가능 : as 별칭
import random as r
print(r.randint(1,6))  # 1부터5사이에 한개만 뽑아옴
print("-"*50)
import math
print(dir(math))    # math모듈안에 모든 함수를 보여줌
print("-"*50)
print(dir(r))

# dir : 모듈안에 모든 함수를 보여주는 명령어
# 테스트 때문에 중간에 사용하지만 import같은건 맨 위쪽으로

# 날짜와 시간을 가져오는 모듈
# 파이썬 - 날짜, html - 날짜, 자바스크립트 - 날짜, db - 날짜
import datetime
now = datetime.datetime.now()
print(now)
print(now.year,"년도")

import time
time.sleep(5)   # 5초동안 대기
print("a")
print("b")

# 패키지 : 모듈파일을 모아둔 폴더
# from Func import *
# 폴더명.모듈명 import 변수, 함수, 클래스, *
# from cal.Func import *
# from 폴더명 import 모듈명
from cal import Func
print(func1())
