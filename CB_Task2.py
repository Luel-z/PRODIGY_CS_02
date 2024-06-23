import string

password = input("Enter the password: ")

upper_case =  any([1 if c in string.ascii_uppercase else 0 for c in password])
lower_case = any([1 if c in string.ascii_lowercase else 0 for c in password])
special =  any([1 if c in string.punctuation else 0 for c in password])
digits = any([1 if c in string.digits else 0 for c in password])

characters = [upper_case, lower_case, special, digits]
length = len(password)

score = 0
with open('passwordlist.txt', 'r') as f:
    common = f.read().splitlines()

if password in common:
    print("Password was found in a common list.")
    exit()

if length >8:
    score +=1
if length >9:
    score +=1
if length >10:
    score +=1
if length >11:
    score +=1
print(f"Password length is {str(length)}, adding {str(score)} points!")

if sum(characters) > 1:
    score +=1
if sum(characters) > 2:
    score +=1
if sum(characters) > 3:
    score +=1
print(f"Password has {str(sum(characters))} different character types, adding {str(sum(characters) - 1)} points!")

if score < 4:
    print(f"The password is weak! score: {str(score)} / 7")
elif score == 4:
    print(f"The password is Ok! score: {str(score)} / 7")
elif 4 < score < 6:
    print(f"The password is Good! score: {str(score)} / 7")
    exit()
elif score >= 6:
    print(f"The password is Strong! score: {str(score)} / 7")