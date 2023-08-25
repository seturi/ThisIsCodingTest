array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

# 파이썬 특화 ver.
def quick_sort(array):
		# 리스트가 하나 이하의 원소만을 담고 있다면 종료
		if len(array) <= 1:
				return array
		pivot = array[0]
		tail = array[1:]
		
		left_side = [x for x in tail if x <= pivot] # 분할된 왼쪽 부분
		right_side = [x for x in tail if x > pivot] # 분할된 오른쪽 부분
	
		# 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행하고, 전체 리스트 반환
		return quick_sort(left_side) + [pivot] + quick_sort(right_side)

print(quick__sort(array))