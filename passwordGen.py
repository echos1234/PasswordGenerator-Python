import time
from random import sample, choice
import secrets
import string
import json

#defining the things that will be used
symbols = "?*&%$#!"
letters = string.ascii_letters + string.digits + symbols
blue = "\u001b[34m"
red_flashing = "\u001b[31;5m"
escape_proof = "\033[0m"

#ansi colors
print(blue)

#Dialog
print("So, you want a password")

time.sleep(1)

question = input("(yes) (No) ").lower()

while question != ("yes".lower() or "no".lower()):
    print("Sorry, Thats not (yes) or (no)")
    time.sleep(1)
    question = input("(yes) (No) ").lower()

if question != "yes".lower():
    quit()

#Dialog + sleep for better flow
else:
    print("Loading current saved passwords...")

time.sleep(1)

print("Saved Passwords:")

time.sleep(1)

#Attempts to load off of your json file, if it fails it moves on
f = open("passwords.json", "r")

def json_loads_stuff():
    try:
       the_items = json.load(f)
    except:
        print("No previous passwords were found, save a password to load previous")
        the_items = []
    finally:
        return the_items

items = json_loads_stuff()

#ansi colors + printing the pass and name of old pass's
print(red_flashing)


f.close()
for item in items:
    print(item)

time.sleep(1)

#Adding a name for the password for later use in files + ansi colors
#print("\u001b[34m" + "\033[0m")
print(escape_proof + blue)
sign_up_name = input("What are you signing up for? ")

time.sleep(1)

#Length of pass + generating and printing it
password_length = input("How long should your password be? (integer format) ")

while not password_length.isdigit():
    print("Sorry that isn't a valid format, please input an integer")
    time.sleep(1)
    password_length = input("How long should your password be? (integer format) ")

password = ''.join(secrets.choice(letters) for bruh in range(int(password_length)))
print(sign_up_name + str(": ") + password)

#items
new_item = {
    "Company": sign_up_name,
    "Password": password
}

#Dumping the password and name to your json file
items.append(new_item)
items_json = json.dumps(items)

f = open("passwords.json", "w")
f.write(items_json)
f.close()

time.sleep(1)
#end
print("Your password has been saved, if the program is reloaded your password(s) will be displayed")
quit()
