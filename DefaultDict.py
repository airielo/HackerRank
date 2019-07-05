
from collections import defaultdict
# Desctructuring the input into two variables n, m. By calling split(), we make an initial
# string input a list
n, m = input().split()

# Creating a defaultdict with items lists so that we can call list functions on them
d=defaultdict(list)
# Example:
# d['python'].append("awesome")
# d['something-else'].append("not relevant")
# d['python'].append("language")
# for i in d.items():
#  print i

# Considering that our input has many lines and input provides one line at a time
# we have to loop through all the elements of the input
for i in range(1, int(n)+1):
   # d[input()] is our key and its corresponding list of items is all the i 
   # related to this key which we append to the dictionary
    d[input()].append(i)

for j in range(1, int(m)+1):
    # We are saving the input to be able to reuse it later again
    key = input()
    # Here we are checking whether a character in "key" exists in the dictionary
    # that we created before 
    if key in d.keys():
        # If it does exist, we print indices
        # We used map to make sure that all the passed variables into the join are char
        # otherwise it throws out an error message
        print(" ".join(map(str, d[key])))
    else:
        # If the element doesnt exist in the dictionary,
        # -1 is printed
        print ("-1")



