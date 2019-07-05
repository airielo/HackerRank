# Reading in integer input
n = input()

s=set()
# Looping for a n number times specified by the user input and adding 
# subsequent user input strings into a set
# example of a user input:
# 7 - is our n
# UK - consequent string values
# China
# USA
# France
# New Zealand
# UK
# France 
for i in range(int(n)):
    s.add(str(input()))

print (len(s))