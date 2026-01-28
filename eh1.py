try:

    a = int(input("enter first no "))
    b = int(input("enter second no "))
    c = a/b
    print("division is ",c)
except ValueError:
    print("please enter numbers only")
except ZeroDivisionError:
    print("you cannot divide any no by 0")