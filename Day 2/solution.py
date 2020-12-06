# function to retrieve passwords from data file.
def get_passwords():
    with open("data.txt", 'r') as input_file:
        lines = input_file.readlines()
    return lines

# function to validate passwords based upon day 2 guide part 1
# example line: 1-3 a: abcde
# 1-3 a means that the password must contain a at least 1 time and at most 3 times.
def validate_password_old_policy(line):
    limits, letter, passwd = line.split()
    letter = letter[0]
    lower, upper = limits.split("-")
    return int(lower) <= passwd.count(letter) <= int(upper)

# function interate passwords counting valid for part 1
def count_valid_passwords_old_policy():
    lines = get_passwords()
    valid = 0
    for line in lines:
        if validate_password_old_policy(line):
            valid += 1
    return valid

# function to validate passwords based upon day 2 guide part 2
# example line: 1-3 a: abcde 
# is valid: position 1 contains a and position 3 does not.
def validate_password_current_policy(line):
    limits, letter, passwd = line.split()
    letter = letter[0]
    first, second = limits.split("-")
    return (passwd[int(first)-1] == letter) ^ (passwd[int(second)-1] == letter)

# function interate passwords counting valid for part 2
def count_valid_passwords_current_policy():
    lines = get_passwords()
    valid = 0
    for line in lines:
        if validate_password_current_policy(line):
            valid += 1
    return valid


# Part 1
print(count_valid_passwords_old_policy())
# Part 2
print(count_valid_passwords_current_policy())