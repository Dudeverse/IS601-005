import random
import time




n = 100000 # number of elements
num_permutations = 1000# number of permutations to generate

# generate num_permutations random permutations
permutations = []
for i in range(num_permutations):
    permutation = list(range(1, n+1)) # initialize with the identity permutation
    random.shuffle(permutation) # shuffle the elements randomly
    permutations.append(permutation)

# print the first five permutations
for i in range(2):
    print(permutations[i])


def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)

# Example usage







start = time.time()

count = 1
for each_perm in permutations:
    #print(each_perm)
    print("---------count:", count)
    sorted_arr = quick_sort(each_perm)
    count = count + 1
    #print("Sorted array is:", sorted_arr)
    
    
    
end = time.time()
run_time = end - start
print(f"Running time in milliseconds: {run_time*1000} ms" )