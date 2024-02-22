# 문자열 뒤집기

data = list(input())
count0 = 0
count1 = 0

# 첫 번째 원소 처리
if data[0] == '0':
    count0 += 1
else:
    count1 += 1

# 두 번째 원소부터 모든 원소 확인
for i in range(len(data)-1):
    if data[i] != data[i+1]:
        # 다음 수에서 0으로 바뀌는 경우
        if data[i+1] == '0':
            count1 += 1
        # 다음 수에서 1로 바뀌는 경우
        else:
            count0 += 1

print(min(count0, count1))