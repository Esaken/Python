import random
print("Create a strong password:  ")

chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvyxyz1234567890!@#$%&()_'

password = ''
for x in range(20):
    password += random.choice(chars)
    
    
print(password)
