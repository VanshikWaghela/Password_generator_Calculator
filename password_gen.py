import random
import array

print("Do you want your password to be 1.Complex 2.Very complex 3.Extremely complex (Enter 1 or 2 or 3)")
comp_choice = int(input())

# giving user the choice for the length of the password from 8-12 characters
print("Enter number of characters you want to have in your password from 8-12 (longer passwords are generally more secured)")
len_choice = int(input())

digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] 
lowcase_chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
                     'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q',
                     'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
                     'z']
 
upcase_chars = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
                     'I', 'J', 'K', 'M', 'N', 'O', 'P', 'Q',
                     'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
                     'Z']
 
sp_chars = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>',
           '*', '(', ')', '<']
 
 # randomly selecting at least one character from each character set above
rand_digit = random.choice(digits)
rand_upper = random.choice(upcase_chars)
rand_lower = random.choice(lowcase_chars)
rand_sp = random.choice(sp_chars)

if comp_choice == 3:
    print("Do you want to include special characters? (Enter Y or N)")
    sp_choice = input()
    if sp_choice =='Y':
        temp_pass = rand_digit + rand_upper + rand_lower + rand_sp
        pass_list = digits + lowcase_chars + upcase_chars + sp_chars
    elif sp_choice=='N':
       temp_pass = rand_digit + rand_upper + rand_lower
       pass_list = digits + lowcase_chars + upcase_chars  
    else:
        print("Invalid input") 
 
    # we now have 4 digits for our password, now based on the len_choice we will generate remaining characters
    for x in range(len_choice - 4):
        temp_pass = temp_pass + random.choice(pass_list)
 
    # making the temp_pass into an array so that we can shuffle it
    # and avoid the first part of our password having a predictable pattern

    temp_pass_list = array.array('u', temp_pass)
    random.shuffle(temp_pass_list)
 
    # traverse the temporary password to convert it into a word from array
    password = ""
    for x in temp_pass_list:
        password = password + x

# in complexity choice 2, special case option is not provided   
elif comp_choice == 2:

    temp_pass = rand_digit + rand_lower + rand_upper
    pass_list = digits + lowcase_chars + upcase_chars 
    
 # we now have 3 digits for our password, now based on the len_choice we will generate remaining characters
    for x in range(len_choice - 3):
        temp_pass = temp_pass + random.choice(pass_list)
 
    temp_pass_list = array.array('u', temp_pass)
    random.shuffle(temp_pass_list)
 
    password = ""
    for x in temp_pass_list:
        password = password + x

# in 1 complexity only digits and lowercase options are available
elif comp_choice == 1:
    
    pass_list = digits + lowcase_chars
    temp_pass = rand_digit + rand_lower
 
    # we now have 2 digits for our password, now based on the len_choice we will generate remaining characters
    for x in range(len_choice - 2):
       temp_pass = temp_pass + random.choice(pass_list)
    temp_pass_list = array.array('u', temp_pass)
    random.shuffle(temp_pass_list)
 
    password = ""
    for x in temp_pass_list:
        password = password + x
else:
    print("Invalid choice")

print(password)