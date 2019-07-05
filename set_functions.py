n = int(input())
s = set(map(int, input().split()))
n_commands = int(input())

for i in range(n_commands):
    variable = input().split()
    if variable[0] == "pop":
        s.pop()

    if variable[0] == "remove":
        s.remove(int(variable[1]))

    if variable[0] == "discard":
        s.discard(int(variable[1]))


print(sum(s))