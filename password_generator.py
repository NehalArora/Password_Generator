import random

max_length = 12

digits = ['1','2','3','4','5','6','7','8','9','0']
small_letter = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
capital_letter =  ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
symbol = ['!','@','#','$','%','^','&','*','(',')','\\','|','/','?','~']

combined_list = digits + small_letter + capital_letter + symbol

rand_digit = random.choice(digits)
rand_small_letter = random.choice(small_letter)
rand_capital_letter = random.choice(capital_letter)
rand_symbol = random.choice(symbol)

#combining all the above lists 
password = rand_symbol + rand_capital_letter + rand_digit + rand_small_letter 

for i in range (max_length - 4):
    password += random.choice(combined_list)

print(password)