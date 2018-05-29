def bubble_sort(input):
    size = len(input)
    for j in range(size):
        for i in range(size-j-1):
            if input[i]> input[i+1]:
                input[i], input[i+1]= input[i+1], input[i]
    return input
                
print(bubble_sort([9, 10, 4, 8, 1]))