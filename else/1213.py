s = input()
arr = list(s)
length = len(arr)
arr.sort()
for i, item in enumerate(arr):
	print(i,"i",item,"item")
	if i+1 <= length // 2:
		if arr.count(item) % 2 == 1:
			if length % 2 == 0:
				print("I'm Sorry Hansoo")
				break
			else:
				print("HERE")
				arr[i], arr[length % 2 + 1] = arr[length % 2 + 1], arr[i]
			print(arr, "arr")
		else:
			print("changearr", arr[i+1:])
			temp = arr[i:].index(item) + i + 1
			print("i", i, "temp", temp)
			arr[temp], arr[length-i-1] = arr[length-i-1], arr[temp]
		print(arr, "arr2")
		