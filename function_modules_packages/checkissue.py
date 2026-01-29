def add_item(item,shopping_list=None):
    if shopping_list is None:
        shopping_list=[]

    shopping_list.append(item)
    return shopping_list
def checkout(total):
    if(total==0):
        print("nothing to checkout")
    elif total<0:
        print("err")
    else:
        # print("Toal is $",total)
        print(f"total is $ ${total}")

items = add_item("apple")
items= add_item("banana",items)
items = add_item("orange",items)
items=add_item("apple",items)
total = 0 
print(items)
for i in items:
    total+=5
checkout(total)
# def is_even(num):
#     if num % 2 == 1:
#         return True
#     else:
#         return False

# print(is_even(4))
def add_item(item,shopping_list=[]):
    shopping_list.append(item)
    return shopping_list
def checkout(total):
    if(total==0):
        print("nothing to checkout")
    elif total<0:
        print("err")
    else:
        print("Toal is $",total)

items = add_item("apple")
item= add_item("banana")
total = 0 
for i in items:
    total+=5
checkout(total)
# def is_even(num):
#     if num % 2 == 1:
#         return True
#     else:
#         return False

# print(is_even(4))
def add_item(item,shopping_list=[]):
    shopping_list.append(item)
    return shopping_list
def checkout(total):
    if(total==0):
        print("nothing to checkout")
    elif total<0:
        print("err")
    else:
        print("Toal is $",total)

items = add_item("apple")
item= add_item("banana")
total = 0 
for i in items:
    total+=5
checkout(total)
# def is_even(num):
#     if num % 2 == 1:
#         return True
#     else:
#         return False

# print(is_even(4))
 The instructor presents a real-world problem, 
e.g., "Design the data model for a simple social media post, "
"which has content, an author, "
 "a list of users who liked it, and a list of comments."
# post = {content:"",author:"", likedby:[],comments:[{by:,commment:}]}