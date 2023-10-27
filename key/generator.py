import string
import random
string.ascii_letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!§$%&/([=?@€+*#-_:,;<>1234567890áéíóúÁÉÍÓÚâêîôûÂÊÎÔßöÖäÄüÜ '
#List of sting.ascii_letters
print(list(string.ascii_letters))
print(len(string.ascii_letters))


def generate(key=""):
    while len(key) < 111:
        randomValue = random.choice(string.ascii_letters)
        if randomValue not in key:
            key += randomValue
    print("key: " + key)
    return key

generate()