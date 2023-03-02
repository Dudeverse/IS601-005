import random
import time

#tune n to higher numbers to see how the running time changes


n = 1000 # number of elements
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


# Python program for implementation of Cocktail Sort

def cocktailSort(a):
	n = len(a)
	swapped = True
	start = 0
	end = n-1
	while (swapped==True):

		# reset the swapped flag on entering the loop,
		# because it might be true from a previous
		# iteration.
		swapped = False

		# loop from left to right same as the bubble
		# sort
		for i in range (start, end):
			if (a[i] < a[i+1]) :
				a[i], a[i+1]= a[i+1], a[i]
				swapped=True

		# if nothing moved, then array is sorted.
		if (swapped==False):
			break

		# otherwise, reset the swapped flag so that it
		# can be used in the next stage
		swapped = False

		# move the end point back by one, because
		# item at the end is in its rightful spot
		end = end-1

		# from right to left, doing the same
		# comparison as in the previous stage
		for i in range(end-1, start-1,-1):
			if (a[i] < a[i+1]):
				a[i], a[i+1] = a[i+1], a[i]
				swapped = True

		# increase the starting point, because
		# the last stage would have moved the next
		# smallest number to its rightful spot.
		start = start+1

# Driver code to test above

start = time.time()

count = 1
for each_perm in permutations:
    #start = time.time()
    print("---------count:", count)
    print(each_perm)
    cocktailSort(each_perm)
    print("Sorted array is:", each_perm)
    count = count + 1
    each_perm.sort()
    print(each_perm)
    #end = time.time()
    #run_time = end - start
    #print(f"Running time in milliseconds: {run_time*1000} ms" )
    
    
end = time.time()
run_time = end - start
print(f"Running time in milliseconds: {run_time*1000} ms" )