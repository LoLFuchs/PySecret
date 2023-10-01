import string
string.ascii_letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!§$%&/([=?@€+*#-_:,;<>1234567890'
import random
random.choice(string.ascii_letters)

key = ""
def generate(key = ""):
    while len(list(key)) < 76:
        randomValue = random.choice(string.ascii_letters)
        if randomValue not in list(key):
            key += randomValue
        else:
            pass
    print("key: " + key)
    return key

generate()