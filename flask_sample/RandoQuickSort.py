import random
import time




n = 100# number of elements
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



def randomized_quick_sort(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = random.choice(arr)
    left, equal, right = [], [], []
    
    for num in arr:
        if num < pivot:
            left.append(num)
        elif num == pivot:
            equal.append(num)
        else:
            right.append(num)
    
    return randomized_quick_sort(left) + equal + randomized_quick_sort(right)







start = time.time()

count = 1
for each_perm in permutations:
    print(each_perm)
    print("---------count:", count)
    sorted_arr = randomized_quick_sort(each_perm)
    count = count + 1
    print("Sorted array is:", sorted_arr)
    
    
    
end = time.time()
run_time = end - start
print(f"Running time in milliseconds: {run_time*1000} ms" )