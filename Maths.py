import math
marks = [25,36,45,34,29,46]
sum_marks = math.fsum(marks)
print("sum is ",sum_marks)
length = len(marks)
print("length is ",length)
avg_marks = sum_marks/length
print("average is ",math.floor (avg_marks))