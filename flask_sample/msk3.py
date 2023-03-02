import random
import time

import sys
sys.setrecursionlimit(10000)
print(sys.getrecursionlimit())

#tune n to higher numbers to see how the running time changes

n = 10000 # number of elements
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
        if len(arr) <= 3:
            # use insertion sort for small subarrays
            for i in range(1, len(arr)):
                j = i
                while j > 0 and arr[j-1] > arr[j]:
                    arr[j-1], arr[j] = arr[j], arr[j-1]
                    j -= 1
            return arr
        else:
            # divide the array into three parts
            m = len(arr) // 3
            left = merge_sort(arr[:m])
            middle = merge_sort(arr[m:2*m])
            right = merge_sort(arr[2*m:])
            # merge the three parts
            i = j = k = 0
            while i < len(left) and j < len(middle) and k < len(right):
                if left[i] < middle[j]:
                    if left[i] < right[k]:
                        arr[i+j+k] = left[i]
                        i += 1
                    else:
                        arr[i+j+k] = right[k]
                        k += 1
                else:
                    if middle[j] < right[k]:
                        arr[i+j+k] = middle[j]
                        j += 1
                    else:
                        arr[i+j+k] = right[k]
                        k += 1
            # merge any remaining elements
            while i < len(left) and j < len(middle):
                if left[i] < middle[j]:
                    arr[i+j+k] = left[i]
                    i += 1
                else:
                    arr[i+j+k] = middle[j]
                    j += 1
            while i < len(left) and k < len(right):
                if left[i] < right[k]:
                    arr[i+j+k] = left[i]
                    i += 1
                else:
                    arr[i+j+k] = right[k]
                    k += 1
            while j < len(middle) and k < len(right):
                if middle[j] < right[k]:
                    arr[i+j+k] = middle[j]
                    j += 1
                else:
                    arr[i+j+k] = right[k]
                    k += 1
            # append any remaining elements
            while i < len(left):
                arr[i+j+k] = left[i]
                i += 1
            while j < len(middle):
                arr[i+j+k] = middle[j]
                j += 1
            while k < len(right):
                arr[i+j+k] = right[k]
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