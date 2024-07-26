import random
letters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
symbols=['!','@','#','$','%','^','&','*','(',')']
numbers=['0','1','2','3','4','5','6','7','8','9']
print("WELCOME TO PASSWORD GENERATOR")
length=int(input("Length of the passworrd: "))
n_letters=int(input("How many letters? "))
n_numbers=int(input("How many numbers? "))
n_symbols=int(input("How many symbols? "))
password_list=[]
for i in range(0,n_letters):
    char=random.choice(letters)
    password_list += char
for i in range(0,n_symbols):
    char=random.choice(symbols)
    password_list += char
for i in range(0,n_numbers):
    char=random.choice(numbers)
    password_list += char
random.shuffle(password_list)
password=""
for char in password_list:
    password=password+char
if length<len(password)or length>len(password):
    print("Length doesn't match")
    quit()
print(f"The Password is: {password}")


