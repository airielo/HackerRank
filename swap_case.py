def swap_case(s):
    s=list(s)
    for i, c in enumerate(s):
        if c.isupper()==True:
           s[i] = c.lower()
            
        else:
            s[i]=c.upper()
            
    return "".join(s)

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)