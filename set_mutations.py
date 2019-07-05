n_of_list = int(input())
first_set = set(map(int, input().split()))
n_sets = input()

for i in range(int(n_sets)):
    # Destructuring the input
    operation, length = input().split()
    # Turning the input into a string, then a set
    # + making sure all the elements are integers
    second_set = set(map(int, input().split()))

    if operation == "intersection_update":
        first_set.intersection_update(second_set)
    
    if operation == "update":
        first_set.update(second_set)

    if operation == "symmetric_difference_update":
        first_set.symmetric_difference_update(second_set)
     
    if operation == "difference_update":
        first_set.difference_update(second_set)
    

print(sum(first_set))

