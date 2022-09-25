a1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
a2 = [0, 1, 3, 5, 7, 9, 2, 4, 6, 8, 10]
a3 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
a4 = [0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10]


def process_array(num, arr):
    print("\nProcessing Array({}): \n\n".format(num))
    print(arr)
    print("\nOdds output:\n")
    Odds_list=[arr[i] for i in range(len(arr)) if arr[i]%2!=0]
    print(Odds_list)
    # UCID - se352, date - Sept 25th, 2022, tried to write in single line but I had to use two lines.
    # As soon as I read the hint, I knew I had to use comprehensions. 
    # Using a list comprehension, a simple technique to write loops and conditions with minimal syntax, 
    # I tried to make a list of odd values. "i" is used to iterate through the list and "arr[i]" is used to check if
    # the value is odd or not. If it is odd, it must not be divisible by 0, hence arr[i]%2!=0.
    # Python is very much like English, so writing comprehensions in python
    #  is almost just like writing a passage in English that makes sense. 


print("Problem 1")
process_array(1, a1)
process_array(2, a2)
process_array(3, a3)
process_array(4, a4)