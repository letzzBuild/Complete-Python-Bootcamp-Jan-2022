noofRows = 5
noofColumns = 5

#Pattern 1 
# for rows in range(1,noofRows + 1): 
#     for columns in range(1,noofColumns + 1):
#         print("*",end="") 
#     print("\n") 
#    

#Pattern 2
# for rows in range(1,noofRows + 1):
#     for columns in range(1,rows + 1):
#         print("*",end="")
#     print("\n") 
# 


#Pattern 3
# for rows in range(1,noofRows+1):
#     for columns in range(1,rows+1):
#         print(columns,end="")
#     print("\n")  
# 

#Pattern 4
# for rows in range(1,noofRows+1):
#     for space in range(1,(noofRows-rows)+1):
#         print(" ",end="")
#     for columns in range(1,rows+1):
#         print(columns,end="")
#     print("\n")


#Pattern 5
# for rows in range(1,noofRows+1):
#     for columns in range(1,noofRows-rows+1):
#         print(columns,end="")
#     print("\n") 


#Pattern 5
# for rows in range(1,noofRows+1):
#     for space in range(1,(noofRows-rows)+1):
#         print(" ",end="")
#     for columns in range(1,rows+1):
#         print("* ",end="")
#     print("\n") 


#check if number is palindrome
# 1234 == 4321
# 1111 == 1111

# n = 342
# temp = n
# reverse = 0
# while(n>0):
#     r = n%10
#     n = int(n/10)
#     reverse = reverse*10 + r

# if reverse == temp:
#     print("palindrome")
# else:
#     print("not palindrome")    








