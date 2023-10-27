import string
import random
string.ascii_letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!§$%&/()[]"=?@€+*#-_:.,;<>1234567890áéíóúÁÉÍÓÚâêîôûÂÊÎÔßöÖäÄüÜ '


def generate(key=""):
    while len(key) < 115:
        randomValue = random.choice(string.ascii_letters)
        if randomValue not in key:
            key += randomValue
    return key

generate()