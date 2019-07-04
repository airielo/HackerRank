def count_substring(string, sub_string):
    counter=0 #counter will show a number of times a subtring was matched

    # For each character in 'string'
    for i in range (len(string)): 

        # If the character matches the first character in 'sub_string'
        # then this is the start of a potential sub_string.
        if string[i]==sub_string[0]:

            # From the start of the potential substring to the end of the potential substring
            for j in range(i, len(sub_string)+i): 

                # Making sure the looping will stop once we reach the last element of the string
                if j>len(string)-1:
                    break

                # Since j can be any index in 'string' we need to calculate the
                # index in 'sub_string' e.g. if we are looking at the first character in 
                # a potential substring in 'string', sub_i will represent the corrosponding 
                # index in 'sub_string' so that we can compare the two characters
                sub_i = j-i 

                # If the characters do not match, this potential substring is not a valid substring
                if sub_string[sub_i]!= string[j]:
                    break 

                # If we reach the last element of the potential substring we increment count 
                if j==len(sub_string)+i-1:
                    counter=counter+1   
    return counter

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)