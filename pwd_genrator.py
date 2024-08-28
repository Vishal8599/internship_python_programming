import random
import string

def genrate_pwd(length, use_uppescase=True,use_digit=True,use_special=True):
    character=string.ascii_lowercase
    if use_uppescase:
        character += string.ascii_uppercase
    if use_digit:
        character += string.digits
    if use_special:
        character += string.punctuation


    pwd = ''.join(random.choice(character) for i in range(length) )
    return pwd


length= int(input("enter the length of password "))
use_uppescase = input("include uppercase letters ? yes/no:").lower() =="yes"
use_digit = input("include digit? yes/no:").lower() == 'yes'
use_special =input("include special character? yes/no:").lower() =='yes'

pwd =genrate_pwd(length, use_uppescase,use_digit,use_special)
    ###############################################################
print(f"genrated password:{pwd}")