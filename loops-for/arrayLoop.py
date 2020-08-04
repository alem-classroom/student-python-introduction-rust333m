def insert_squares(arr, num):
    	arr = int(input())
	arr2 = []
	for i in range(1,num+1):
		arr2.append(i ** 2)
	print(arr + arr2)
    # add square of numbers from 1 to num to the list named arr and return list
