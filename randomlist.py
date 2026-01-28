# Write a script that generates a list of 6 unique random numbers 
# between 1 and 49, simulating a lottery draw. Use sample().
import random
random_list = random.sample(range(1,50),6)
print(random_list)