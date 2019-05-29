# Python program to reverse a string without stack 
# Function to reverse a string 
def forthReverseString(string):
    string = "".join(reversed(string))
    return string


str = input("Plase enter the string    ")
rev_str = forthReverseString(str)
print("Original String is : ", str, "   And Reverse String is : ", rev_str)
