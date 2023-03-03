import random
import time
import math
import sys
sys.setrecursionlimit(10000)
print(sys.getrecursionlimit())

#tune n to higher numbers to see how the running time changes

n = 10 # number of elements
num_permutations = 10 # number of permutations to generate

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

import math

def merge_sort_k_2_5(arr):
    if len(arr) <= 1:
        return arr
    
    k = 2/5
    n = len(arr)
    subarray_size = math.ceil(n * k)
    subarrays = [arr[i:i+subarray_size] for i in range(0, n, subarray_size)]
    
    sorted_subarrays = [merge_sort_k_2_5(subarray) for subarray in subarrays]
    sorted_arr = merge_sorted_subarrays(sorted_subarrays)
    
    return sorted_arr

def merge_sorted_subarrays(sorted_subarrays):
    if len(sorted_subarrays) == 1:
        return sorted_subarrays[0]
    
    merged_subarrays = []
    for i in range(0, len(sorted_subarrays), 2):
        if i == len(sorted_subarrays) - 1:
            merged_subarray = sorted_subarrays[i]
        else:
            merged_subarray = merge(sorted_subarrays[i], sorted_subarrays[i+1])
        merged_subarrays.append(merged_subarray)
    
    return merge_sorted_subarrays(merged_subarrays)

def merge(left, right):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]
    return result

# Test the code with the input array [2, 9, 0, 1, 4, 7, 8, 5]
arr = [2, 9, 0, 1, 4, 7, 8, 5]
sorted_arr = merge_sort_k_2_5(arr)
print(sorted_arr)

start = time.time()

count = 1
for each_perm in permutations:
    print("---------count:", count)
    #print(each_perm)
    #print(len(each_perm))
    sorted_arr = merge_sort_k_2_5(each_perm)
    #print("Sorted array is:", sorted_arr)
    #print(len(sorted_arr))
    count = count + 1
    
    
end = time.time()
run_time = end - start
print(f"Running time in milliseconds: {run_time*1000} ms" )