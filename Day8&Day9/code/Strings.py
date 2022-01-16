#raw string
# name = r"hello \t"
# print(name)

#multiple line strings 
# print("""
# Hey i am a string.
# I can be written in multiple lines.
#  """)

#Indexing and slicing in String 
# name = "gautam"
# print(name[-1])
# print(name[-1:])
# 


#in and not operator in string
names ="Ganesh Gautam Shreya Aditya"

# if "Gautam" in names:
#     print("Gautam is in the string")

# if not "Gautam" in names:
#     print("Gautam is not in the string")


#string formating and f strings


#methods/functions in string
name = "Anita Patil"
# print(name.capitalize()) #capatilize 1st letter
# print(name.upper()) #converts to upper case
#print(name.lower()) #converts to lower case
# print(name.swapcase()) #swap case swaps the case of the letters
#print(name.title()) #capitalize first letter of each word

#isX functions in string  ==>always returns boolean values
#print(name.isupper()) #returns true if all the letters are upper case
#print(name.islower()) #returns true if all the letters are lower case
#print(name.isalpha()) #returns true if all the letters are in the string
#print(name.isdigit()) #returns true if all the letters are digits
#print(name.isalnum()) #returns true if all the letters in the string are digits or alphabets
#print(name.isspace()) #returns true if all the letters are spaces
#print(name.istitle()) #returns true if all the letters are in title case


#startswith and endswith
#check if the string starts with a specifice word i.e "hello"
# print(name.startswith("P",7,11)) start and end index are optional
# print(name.endswith("l"))

#join and split methods
# print(name.split(","))  #returns a new list of all splitted words
# print("5".join(["2", "3"]))

#when you want to concatenate elements of a list by adding something in between then use join method
# ["hello", "world"]
# print("=".join("Hello"))

#iterate over a string
# for i in name:
#     print(i)

#ord and chr
# print(ord("A"))#gives ascii value of character
# print(chr(65)) #gives character of the asci value


#strip() function is used to remove white spaces
# words = "  The Helooo    "
# print(words)
# print(words.strip())  #left and right white spaces will be removed
# print(words.lstrip())
# print(words.rstrip())
