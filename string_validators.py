if __name__ == '__main__':
    s = input()

# Alternative solutions:
print(bool(sum([c.isalnum() for c in s])))
print(bool(sum([c.isalpha() for c in s])))
print(bool(sum([c.isdigit() for c in s])))
print(bool(sum([c.islower() for c in s])))
print(bool(sum([c.isupper() for c in s])))

# Check if the string contains any alphanumeric characters
condition_satisfied=False
for c in s:
    if c.isalnum()==True:
        condition_satisfied=True
        break
print(condition_satisfied)

# Check if the string contains any alphabetical characters
condition_satisfied=False
for c in s:
    if c.isalpha()==True:
        condition_satisfied=True
        break
print(condition_satisfied)


# Check if the string contains any digits
condition_satisfied=False
for c in s:
    if c.isdigit()==True:
        condition_satisfied=True
        break
print(condition_satisfied)

# Check if the string contains any lowercase characters
condition_satisfied=False
for c in s:
    if c.islower()==True:
        condition_satisfied=True
        break
print(condition_satisfied)

# Check if the string contains any uppercase characters
condition_satisfied=False
for c in s:
    if c.isupper()==True:
        condition_satisfied=True
        break
print(condition_satisfied)
