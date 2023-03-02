import random
import time

import sys
sys.setrecursionlimit(10000)
print(sys.getrecursionlimit())

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


def merge_sort_p25(arr):
    if len(arr) <= 1:
        return arr

    # Determine the sizes of the two sublists
    p = 2/5
    n = len(arr)
    sublist_size_1 = int(p * n)
    sublist_size_2 = n - sublist_size_1

    # Recursively sort the two sublists
    sublist_1 = merge_sort_p25(arr[:sublist_size_1])
    sublist_2 = merge_sort_p25(arr[sublist_size_1:])

    # Merge the sorted sublists
    merged_arr = []
    i = 0
    j = 0
    while i < len(sublist_1) and j < len(sublist_2):
        if sublist_1[i] < sublist_2[j]:
            merged_arr.append(sublist_1[i])
            i += 1
        else:
            merged_arr.append(sublist_2[j])
            j += 1
    merged_arr += sublist_1[i:]
    merged_arr += sublist_2[j:]

    return merged_arr




start = time.time()

count = 1
for each_perm in permutations:
    print("---------count:", count)
    #print(each_perm)
    #print(len(each_perm))
    sorted_arr = merge_sort_p25(each_perm)
    #print("Sorted array is:", sorted_arr)
    #print(len(sorted_arr))
    count = count + 1
    
    
end = time.time()
run_time = end - start
print(f"Running time in milliseconds: {run_time*1000} ms" )