import random

App = str(input ("Which Application do you want to create a password for:  "))

chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvyxyz1234567890!@#$%&()_"

password = ''
for x in range(20):
    password += random.choice(chars)
    
print("The password for: ", App, "is : ", password)