import string
import random
string.ascii_letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!§$%&/()[]"=?@€+*#-_:.,;<>1234567890áéíóúÁÉÍÓÚâêîôûÂÊÎÔßöÖäÄüÜ '


def generate(key=""):
    while len(key) < len(string.ascii_letters):
        randomValue = random.choice(string.ascii_letters)
        if randomValue not in key:
            key += randomValue
    return key

generate()