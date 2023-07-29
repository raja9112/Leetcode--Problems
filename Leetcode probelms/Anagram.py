# LEVEL : EASY

# Anagram

def anagram(Input1, Input2):

    if( sorted(Input1) == sorted(Input2) ):
        print("It is Anagram")
    else:
        print("It is not Anagram")

val1= input("Enter the value1: ")
val2= input("Enter the value2: ")
anagram(val1, val2)