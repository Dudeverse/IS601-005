import random
import time

#tune n to higher numbers to see how the running time changes


n = 100 # number of elements
num_permutations = 1000 # number of permutations to generate

# generate num_permutations random permutations
permutations = []
for i in range(num_permutations):
    permutation = list(range(1, n+1)) # initialize with the identity permutation
    random.shuffle(permutation) # shuffle the elements randomly
    permutations.append(permutation)

# print the first five permutations
for i in range(2):
    print(permutations[i])

print(len(permutations))
print(type(permutations[0]))
print(type(permutations[0][0]))

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    # recursively sort left and right halves
    left = merge_sort(left)
    right = merge_sort(right)

    # merge the sorted halves
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

        # check if we need to merge adjacent pairs of results
        if len(result) % 2 == 0:
            if result[-2] > result[-1]:
                result[-2], result[-1] = result[-1], result[-2]

    # merge any remaining elements
    result += left[i:]
    result += right[j:]

    # sort adjacent pairs of results
    for i in range(0, len(result)-1, 2):
        if result[i] > result[i+1]:
            result[i], result[i+1] = result[i+1], result[i]

    return result





start = time.time()

count = 1
for each_perm in permutations:
    print("---------count:", count)
    print(each_perm)
    print(len(each_perm))
    sorted_arr = merge_sort(each_perm)
    print("Sorted array is:", sorted_arr)
    print(len(sorted_arr))
    count = count + 1
    
    
end = time.time()
run_time = end - start
print(f"Running time in milliseconds: {run_time*1000} ms" )