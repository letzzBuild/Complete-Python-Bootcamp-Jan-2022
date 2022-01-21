#reverse a string
# name = "Gautam"
# print(name[::-1])

#Not possible
# name = "Name"
# name[0] = "M"

#Question  2 
# word = input("enter some string ")
# n = int(input("enter the index of letter which you want to remove "))
# print(word.replace(word[n],""))

#Question 3
# word = "Abcd"
# reverseStr = word[::-1]
# if word == reverseStr:
#     print("Palindrome")
# else:
#     print("Not Palindrome")
# 


#Question 4
# sentence = input("Enter a sentence")
# wordToCheck = input("Enter a word to search for ")
# if wordToCheck in sentence:
#     print("Word is present")
# else:
#     print("Word is not present")


#Question 5
# sentence = input("Enter a sentence")
# print(sentence.upper())

#Question 6
# string = input("Enter a string : ")
# total = 0
# for i in string:
#     if i.isalpha():
#         total = total + ord(i)

# print(total)
# 


#Question 8
# sentence = input("Enter a sentence : ")
# word = input("Enter a word : ")
# print(sentence.partition(word)) #returns a tuple with three values


#Question 9
# sentence = "Enter a sentence"
# for x in sentence:
#     if x=="a" or x=="e" or x=="i" or x=="o" or x=="u":
#         pass
#     else:
#         print(x)

#Question 10

#Frequency of every letter in a String
# sentence = "Hello this is me"
# for x in sentence:
#     if x.isalpha():
#        print(x,sentence.count(x))

#Find occurance of a given letter in a string
# sentence = "Hello this is me"
# letter = "e"

# print(sentence.count("H"))

operations = ["--X","X++","X++"]
x = 0
for i in operations:
    if i=="X++" or i=="++X":
        x= x+1
    else:
        x = x-1
print(x)            
    


 





