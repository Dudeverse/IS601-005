import random
import time

import sys
sys.setrecursionlimit(10000)
print(sys.getrecursionlimit())


n = 100000 # number of elements
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
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        # recursively sort the left and right halves
        if len(left) > 3:
            left = merge_sort(left)
        if len(right) > 3:
            right = merge_sort(right)

        # merge the sorted halves
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1

    return arr


start = time.time()

count = 1
for each_perm in permutations:
    print("---------count:", count)
    #print(each_perm)
    #print(len(each_perm))
    sorted_arr = merge_sort(each_perm)
    #print("Sorted array is:", sorted_arr)
    #print(len(sorted_arr))
    count = count + 1
    
    
end = time.time()
run_time = end - start
print(f"Running time in milliseconds: {run_time*1000} ms" )