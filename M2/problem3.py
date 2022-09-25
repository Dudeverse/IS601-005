a1 = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10]
a2 = [-1, 1, -2, 2, 3, -3, -4, 5]
a3 = [-0.01, -0.0001, -.15]
a4 = ["-1", "2", "-3", "4", "-5", "5", "-6", "6", "-7", "7"]


def process_array(num, arr):
    print("\nProcessing Array({}): \n\n".format(num))
    print(arr)
    print("\nPositive Output:\n")
    new_list = []
    #UCID - se352, Date - 25th September, 2022. I'll attempt to explain the code at each level of indentation.
    #the for loop below is to traverse across the lists 
    for i in range(len(arr)):
        #Depending upon the type of value, i.e., if the value is an 'int' or 'float' or 'str' 
        if type(arr[i]) is int:
            #if the value is negative
            if (arr[i]) < 0 :
                #make it positive, by using (-) unary negation operator
                x = -(arr[i])
                #and add it to the updated list.
                new_list.append(x)
                new_list.append(type(x))
            else:
                #else keep it as it is
                x = arr[i]
                #and add it to the updated list.
                new_list.append(x)
                new_list.append(type(x))

        elif type(arr[i]) is float:
            #Same goes for float, just like 'int' above
            if (arr[i]) < 0 :
                x = -(arr[i])
                new_list.append(x)
                new_list.append(type(x))
            else:
                x = arr[i]
                new_list.append(x)
                new_list.append(type(x))

        elif type(arr[i]) is str:
            #But when it comes to str, change the type to int
            if int(arr[i]) < 0:
                x = -int((arr[i]))
                #and while updating the list change it back to str
                y = str(x)
                new_list.append(y)
                new_list.append(type(y))
            else:
                x = (arr[i])
                new_list.append(str(x))
                new_list.append(type(x))
    print(new_list)        


print("Problem 3")
process_array(1, a1)
process_array(2, a2)
process_array(3, a3)
process_array(4, a4)