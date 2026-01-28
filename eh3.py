# Write a script that asks the user for their age.
#  Use a ..except ValueError block to handle the 
#  case where they enter non-numeric text. 
# Keep asking until they enter a valid age.
while True:
    try:
        age = int(input("Enter your age"))
        print("your age is ",age)
        break
    except ValueError:
        print("invalid input, Enter valid age")