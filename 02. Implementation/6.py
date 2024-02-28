# 럭키 스트레이트

'''
# sol 1.
n = list(map(int, input()))
mid = len(n) // 2
left, right = n[:mid], n[mid:]

if sum(left) == sum(right):
    print("LUCKY")
else:
    print("READY")
'''

# sol 2.
n = input()
length = len(n)
summary = 0

# 왼쪽 부분의 자릿수 합 더하기
for i in range(length // 2):
    summary += int(n[i])

# 오른쪽 부분의 자릿수 합 빼기
for i in range(length // 2, length):
    summary -= int(n[i])

# 왼쪽 부분과 오른쪽 부분의 자릿수 합이 동일한지 검사
if summary == 0:
    print("LUCKY")
else:
    print("READY")