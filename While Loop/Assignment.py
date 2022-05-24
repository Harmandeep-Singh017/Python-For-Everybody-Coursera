# Write a function, sublist, that takes in a list of numbers as the parameter. In the function, use a while loop to return a sublist of the input list. 
# The sublist should contain the same values of the original list up until it reaches the number 5 (it should not contain the number 5).

def sublist(lis):
    sub = []
    lis = (num for num in lis) 
    n = next(lis, 5)  
    while n != 5:
        sub.append(n)
        n = next(lis, 5)  
    return sub

lis = [1,2,3,4,5,6,7,8,9]
print(sublist(lis))


# Write a function called check_nums that takes a list as its parameter, and contains a while loop that only stops once the element of the list is the number 7. 
# What is returned is a list of all of the numbers up until it reaches 7.

