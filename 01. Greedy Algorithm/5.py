# 큰 수의 법칙

# sol 1.
'''
n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort()         # 입력받은 수들 정렬하기
first = data[n-1]   # 가장 큰 수
second = data[n-2]  # 두번째로 큰 수

result = 0
while True:
    for _ in range(k):  # 가장 큰 수 K번 더하기
        if m == 0:      # m이 0이라면 반복문 탈출
            break
        result += first
        m -= 1  # 더할 때마다 1씩 빼기
    if m == 0:  # m이 0이라면 반복문 탈출
        break
    result += second  # 두 번째로 큰 수를 한 번 더하기
    m -= 1      # 더할 때마다 1씩 빼기

print(result)
'''

# sol 2.
n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort()         # 입력받은 수들 정렬하기
first = data[n-1]   # 가장 큰 수
second = data[n-2]  # 두번째로 큰 수

# 가장 큰 수가 더해지는 횟수 계산
count = int(m / (k + 1)) * k
count += m % (k + 1)

result = 0
result += (count) * first       # 가장 큰 수 더하기
result += (m - count) * second  # 두 번째로 큰 수 더하기

print(result)