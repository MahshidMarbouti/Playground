def array_pair_sum(k, array):
	#O((N^2)
	for i in range(len(array)):
		for j in range(i+1, len(array)):
			if array[i]+ array[j] == k:
				print("({0}. {1})".format(array[i],array[j]), end=" ")
	print()
	
def array_pair_sum_sorted(k, array):
	#still n^2
	array.sort()
	for i in range(len(array)):
		for j in range(i+1, len(array)):
			if array[i]+ array[j] > k:
				break
			if array[i]+ array[j] == k:
				print("({0}. {1})".format(array[i],array[j]), end=" ")
	print()
	

def pair_sum_sorted_optimized(k, array):
	#n*logn (for the sort) + n (for the rest)
	array.sort()
	start= 0
	end = len(array)-1
	while (start < end):
		first = array[start]
		last = array[end]
		if first+ last < k:
			start +=1
		elif first + last > k:
			end -= 1
		else:
			start +=1
			print("({0}. {1})".format(first, last), end="")
	print()

def pair_sum_optimized2(k, array):
	#wrong for now
	seen =[]
	output=[]
	
	for i, n in enumerate(array):	
		f = k-n
		if f in seen:
			output.append([n, f])
		else:
			seen.append(n)
		
	print(output)	
	
array_pair_sum(10, [3, 4, 5, 6, 7]) 
array_pair_sum(8, [3, 4, 5, 4, 4])
array_pair_sum(4, [1, 1, 2, 3, 4] )
array_pair_sum(0, [4,-4])

array_pair_sum_sorted(10, [3, 4, 5, 6, 7]) 
array_pair_sum_sorted(8, [3, 4, 5, 4, 4])
array_pair_sum_sorted(4, [1, 1, 2, 3, 4] )
array_pair_sum_sorted(0, [4,-4])

pair_sum_sorted_optimized(10, [3, 4, 5, 6, 7])
pair_sum_sorted_optimized(8, [3, 4, 5, 4, 4])
pair_sum_sorted_optimized(4, [1, 1, 2, 3, 4])
pair_sum_sorted_optimized(0, [4,-4])

pair_sum_optimized2(10, [3, 4, 5, 6, 7])
pair_sum_optimized2(8, [3, 4, 5, 4, 4])
pair_sum_optimized2(4, [1, 1, 2, 3, 4])
pair_sum_optimized2(0, [4,-4])
