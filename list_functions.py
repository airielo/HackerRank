if __name__ == '__main__':
    N = int(input())
    
l=[]
for i in range(N):
    variable=input().split()
    
    if variable[0]=="insert":
        l.insert(int(variable[1]), int(variable[2]))
    
    if variable[0]=="print":
        print(l)

    if variable[0]=="remove":
        l.remove(int(variable[1]))

    if variable[0]=="append":
        l.append(int(variable[1]))
    
    if variable[0]=="sort":
        l.sort()

    if variable[0]=="pop":
        l.pop()

    if variable[0]=="reverse":
        l.reverse()