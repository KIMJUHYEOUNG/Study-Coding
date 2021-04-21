n,m,l = list(map(int,input().split()))

store = list(map(int,input().split()))

store.append(0)
store.append(l)

store.sort()

left = 0
right = l

while left <= right:
	mid = (left+right) // 2
	new = 0
	for i in range(len(store)-1):
		get_store = (store[i+1] - store[i]) // mid
		if (store[i+1] - store[i]) % mid == 0:
			get_store -= 1
		new += get_store
	if new > m:
		left = mid+1
	else:
		right = mid-1
print(left)
