from m1 import count_vowel,reverse_string
str = input(" enter any string ")
option = input("press1 for vowel count , press 2 for reverse string")
if(option =="1"):
    x = count_vowel(str)
    print("no of vowels in entered string is ",x)
else:
    r = reverse_string(str)
    print("revered string is : ",r)
    