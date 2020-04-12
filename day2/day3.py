# from day1 import func1
import pdb

# # conditions
# x = int(input("Please enter an integer: "))

# if x < 0:
#     x = 0
#     print('Negative changed to zero')
# elif x == 0:
#     print('Zero')
# elif x == 1:
#     print('Single')
# else:
#     print('More')

# One line if clause
# var = 100
# if ( var == 100 ) : print("Value of expression is 100")
# print("Good bye!")

# # python program to illustrate If statement 
# i = 16
# if (i > 15): 
#    print ("10 is less than 15") 
# print ("I am Not in if") 

# python program to illustrate If else statement 
# i = 20; 
# if (i < 15): 
#     print ("i is smaller than 15") 
#     print ("i'm in if Block") 
# else: 
#     print ("i is greater than 15") 
#     print ("i'm in else Block") 
# print ("i'm not in if and not in else Block") 

# python program to illustrate nested If statement 
# i = 10
# if (i == 10): 
#     #  First if statement 
#     if (i < 15): 
#         print ("i is smaller than 15") 
#     # Nested - if statement 
#     # Will only be executed if statement above 
#     # it is true 
#     if (i < 12): 
#         print ("i is smaller than 12 too") 
#     else: 
#         print ("i is greater than 15") 

# loop
# words = ['cat', 'window', 'defenestrate']
# print(words[0])
# print(type(words))
# for w in words:
#     if len(w) >= 6:
#         func1("test1")
#     else:
#         print(w, len(w))

# print(range(5))
# for i in range(5):
#     print(i)

# arr = ['Mary', 'had', 'a', 'little', 'lamb']
# print(len(arr))
# for i in range(len(arr)):
#     print(i, arr[i])

# print(range(2, 10))
# for n in range(2, 10):
#     for x in range(2, 4):
#         # pdb.set_trace()
#         if n % x == 0:
#             print(n, 'equals', x, '*', n//x)
#             break
#         else:
#             # loop fell through without finding a factor
#             print(n, 'is a prime number')

# while
i = 1
while i < 6:
    # for j in range(0,i):
    #     print(j)
    if i == 2:
        print(input("your name: "))
        break
    print(i)
    i += 1