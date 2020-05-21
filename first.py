username = input("Tell your username \n")
password = input("Enter your password \n")

passlen = len(password)

password_secret = '*' * passlen

print(f' hi {username}, your password {password_secret} is {passlen} letter long' )
