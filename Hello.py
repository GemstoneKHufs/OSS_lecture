# 201900776 김보석 컴퓨터전자시스템공학부

#print("Hello, World!!)



# 회문 부문자열 구하는 문제
# 입력문
string = list(input().lower())

# 회문이면 True 반환, 회문 아니면 False반환


def discrim(string):
    if string == string[::-1]:

        return True
    else:
        return False


# 부문자열 저장용 리스트
subString = []
# 문자열 길이
digit = len(string)
noRotate = 1  # 회문이 없을 때
# 글자수만큼 반복
for i in range(len(string)):
    for j in range(len(string) - (digit - 1)):  # 문자열길이 - (슬라이스한 글자수 -1)만큼 반복
        if discrim(string[j:j+digit]):  # digit 길이에 따라 반복 수 변화
            # 부문자열이 회문일경우 subString에 저장
            subString.append(''.join(string[j:j+digit]))
            noRotate = 0  # 회문이 있을 때 0
    if noRotate == 0:  # 회문이 있으면 for 문 탈출
        break
    digit += -1  # 자릿수 하나 줄이기

subString = sorted(list(set(subString)))  # 중복 제거 후 리스트 변환후 정렬

for i in subString:  # subString 요소 출력 띄어쓰기
    print(i, end=' ')
