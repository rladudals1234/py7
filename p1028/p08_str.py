a = "안녕"
b = '안녕'
print(type(b))

c="aaa\
bbb\
ccc"
print(c)

d="""aaa
bbb
ccc"""
print(d)

student1 = [90,95,85,80]
print(len(student1))
print(type(student1))
print(student1[-1]) # 마지막 값
print(student1*3)

name_list = ["홍","유","이","김","강"]
if("이" in name_list):
    print("이가 있습니다.")
else:
    print("이가 없습니다.")

str1 = "안녕하세요 반갑습니다."
if("반" in str1):
    print("반이 있습니다.")
else:
    print("반이 없습니다.")

num_list = [1,2,3,1,2,3,1,1,1,2,3,2,2,2,2,2]
print(num_list.count(1))
n_list = [4,23,2,9,10,5,7,1]
n_list.sort()       # 순차정렬 - 낮은 값으로 정렬(asc)
print(n_list)
n_list.sort(reverse=True)   # 역순정렬 - 높은값으로 정렬(desc)
print(n_list)
n_list.reverse()    # 정렬이 아닌 순서를 역순으로 출력(정렬없이 역순)
print(n_list)
print(n_list.index(5))  # 정렬 후 3번째 인덱스에 위치해서 3이 나옴

a = 95
if a>90:
    pass    #아무일도 일어나지 않음(아무것도 안 넣고  싶을 때 넣으면 됨)

# score = 99
# hak = ""
# if score>=90:
#     hak = "A"
#     if score>=99:
#         hak=hak+"+"
#     elif score<93:
#         hak=hak+"-"
# if score>=80:
#     hak = "B"
#     if score>=88:
#         hak=hak+"+"
#     elif score<83:
#         hak=hak+"-"
# print(hak)

# if score>=96:
#     print("A+")
# elif score>=93:
#     print("A")
# elif score>=90:
#     print("A-")

a_list = [3,5,9,10,2]
aa_list = []
for i in a_list:
    aa_list.append(i*10)
print(a_list)
print(aa_list)

a="0"
int(a)
print(list(range(10)))
print(list("0"*10))

b_list = list(range(10))
print(b_list)

bb_list = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
bb_list = list(range(100))
