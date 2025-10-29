while True:
    # 반복시작 -----------
    strs = ['이름', '국어', '영어', '수학']
    stu_list = [input(f"{strs[0]}을 입력하세요:")]
    scores = [int(input(f"{subject} 점수를 입력하세요:")) for subject in strs[1:]]
    total = sum(scores)
    stu_list += scores + [total, total / len(scores)]
    print(stu_list)
