# LEVEL : EASY

# Palindrome

def palindrome(Input):

    if (str(Input)==str(Input)[::1]):
        print("Palindrome")
    else:
        print("Not palindrome")

Input=input("Enter the value: ")
palindrome(Input)
