# 예외처리 - 오류(에러), 예외
# 예외처리 - 오류(에러)가 나도 프로그램을 종료하지 않고 계속 실행

# 오류 - 구문오류, 런타임오류
a = 10
print(a)

# prin(a) # 구문오류(실행하기전에 에러남)
a_list = [1,2,3]
print(a_list[0])
# 예외처리 - 외부연결 : 파일입출력, 파일읽기, 쓰기, 프린터기 연결, DB연결
try:
    print(a_list[100]) # 실행을 해야 알 수 있음 - 런타임오류
except Exception as e:
    print("에러 :",e)
    print("예외가 발생했습니다.")
print("프로그램을 종료합니다.")

print(1)
print(2)
try:
    print(3)
    print(4)
    # 에러
    raise SyntaxError   # 강제로 에러발생하는 명령어
    print(5)
except: # 에러발생시 실행
    print(6)
finally:    # 에러 유무와 상관없이 무조건 실행(에러가 발생해도 사용하고 싶은것만)
    print(7)
print(8)


try:
    # 숫자를 입력받습니다.
    number_input = int(input("정수 입력> "))
except ValueError as val_e:
    # ValueError가 발생하는 경우
    print("정수를 입력해주세요!")
except IndexError as inx_e:
    # IndexError가 발생하는 경우
    print("리스트의 인덱스를 벗어났어요!")
