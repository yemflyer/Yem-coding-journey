#random password generator 
# Building process

    #Collect user preferences
''' 
1. length of password
2. should contain uppercase
3. should contain special
4. should contain digits/numbers'''

#App goal = randomly select character out of the available characters we have to pick from, the user preferences create the final group of characters we can pick from

# once we know the pull of character we can pick them 1 by 1 randomly up to the desired length
# make sure that we have at least one of each character type if the user wants them = whatever they select 
# ensure lenght is valid 

#APP TARGET
#Get all available characters
# randomly pick characters up to the length
# ensure we have at least one of eaqch character type
# ensure length is valid

     #Potential error cases:
#1. user only want length =2 but specify all 4 characters types
'''After gathering all info above we have a decent enough plan so we can start coding this out '''
import random # import random #give us access to random functions
import string #give us acces to a list of all the chracters that are lowercase, uppercase, digits or special characters (save us time from having to type them out all manually ourselves)

    
def generate_password():
    length = int(input("Enter the desired password length: ").strip())  
    uppercase = input("Do you want uppercase letters? (y/n): ").strip().lower()
    special = input("Do you want special characters? (y/n): ").strip().lower()
    digits = input("Do you want digits? (y/n): ").strip().lower()   
    
    
    #ensure length is valid
    if length < 4:
        print("Password length must be at least 4")
        return #return exits the function if the length is less than 4
    #anything ran here will not run due to the return exit characteristic of the function if the condition is not met
#Get all available characters
    lower = string.ascii_lowercase #get all lowercase letters
    upper = string.ascii_uppercase if uppercase == 'y' else '' #get all uppercase letters if the user wants them #if the user does not want them, return an empty string
    special_characters = string.punctuation if special =='y' else ''
    digits = string.digits if digits =='y' else ''#Combine all characters

    all_characters = lower + upper + special_characters + digits #Combine all characters = string concatenation

#Ensure we have at least one of each character type
    required_characters = []#use a list why? can keep adding value easily ,convert into string later , shuffle it and join it#Efficiency concern?

    if uppercase == 'y':
        required_characters.append(random.choice(upper)) #append a random uppercase letter to the required characters list
    if special == 'y':
        required_characters.append(random.choice(special_characters)) #append a random special character to the required characters list
    if digits == 'y':
        required_characters.append(random.choice(digits))   #append a random digit to the required characters list

#Fill the rest of the password length with random characters
    remaining_length = length - len(required_characters) #get the remaining length of the password
    password = required_characters
# Pick new random characters to add inside the password currently filled with required_characters from the pool of user preferences
    for _ in range(remaining_length): #loop through the remaining length of the password ,
         # _ is a placeholder variable- we don't need to use it just want the for loop to run for the length of remaining_length
        characters = random.choice(all_characters)  
        password.append(characters)
#dont want the selected character to always be at the beginning of the password so want to reshuffle 
    random.shuffle(password) #shuffle/randomly mixup the password list

#Convert the password list to a string
#why? because we want to print the password as a string not a list
    str_password = ''.join(password) #Very useful method to know in python if added character , it will be added between the characters
    return str_password #return = gives it back to whereever the function was called

#exit the function and return the password as a string
password = generate_password( ) #call the function to generate the password
print (password) #print the password list to see the characters inside the password


generate_password() #call the function to generate the password2

#Convert length to a number
#length = int(length) #convert the lenght to an int why?By default when user type , it is a string# we need to convert it to an int so we can do math with it .
#  replaced by length = int(length) in the next cell

#test1
#generate_password() #Test 1: open terminal + call function and go through the input field
#Test2 print all characters             


'''List of error 
# had the core of the function outside of the function it self causing error NameError: name 'uppercase' is not defined
# format of print(password) not what i want 
Do you want digits? (y/n): y
['Z', '1']
['Z', '1', 'm']
['Z', '1', 'm', 'R']
['Z', '1', 'm', 'R', 'N']
['Z', '1', 'm', 'R', 'N', 'x']
['Z', '1', 'm', 'R', 'N', 'x', 'K']
['Z', '1', 'm', 'R', 'N', 'x', 'K', 'P']
['Z', '1', 'm', 'R', 'N', 'x', 'K', 'P', '1']
['Z', '1', 'm', 'R', 'N', 'x', 'K', 'P', '1', '4']
why? # because password is a list and we are printing the list
#Solution: print(''.join(password)) #join the list into a string and print it
#still printing multiple list 
#%
#%~
#%~|
#%~|l
#%~|lb
#%~|lb9
#%~|lb9;
#%~|lb9;?
#%~|lb9;?d
why?# because we are printing the password inside the for loop
#Solution: print(''.join(password)) #join the list into a string and print it
#FIXED 
Enter the desired password length: 10
Do you want uppercase letters? (y/n): Y
Do you want special characters? (y/n): Y
Do you want digits? (y/n): Y
B~sf}zXCS)
'''