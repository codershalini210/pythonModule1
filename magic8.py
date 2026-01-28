# Create a "Magic 8-Ball" program. 
# Create a list of possible string answers
# and use choice() to select
# and print one each time the user asks a question

import random
possible_answers=["yes",
                  "no",
                  "may be",
                  "Sure",
                  "absolutly",
                  "try again",
                  "doubtful",
                  "noway"]
que = input("Ask the Magic 8-ball a question")
ans =random.choice(possible_answers)
print("Magic 8-balls says: ",ans)