import string
import random
uppercase = string.ascii_uppercase
lowercase = string.ascii_lowercase
digits = string.digits
punctuation = string.punctuation
try:
    while 1==1:
        number = int(input("Write how many characters your password should contain: "))
        print("Your password is: " + ''.join(random.choice(uppercase + lowercase + digits + punctuation) for i in range(int(number))))
except Exception as e:
    print(e)
    print("Start script again and be sure to write integer while being asked for input")