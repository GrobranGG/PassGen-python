# PassGen (v.1) by GrobranGG
import random
import colorama
import secrets

from colorama import init
from colorama import Fore, Back
from random import randint
init()

print(Fore.CYAN + "PassGen v.1 (by GrobranGG)")
print(Back.WHITE)
print(Fore.BLACK + "Choose a language (number):")
print("1. English")
print("2. Russian")

print(Back.RESET)
print(Fore.CYAN)
language = input("Enter your language: ")
chars = '+-/*!&$#?=@<>abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'

if language == "1":
    number = int(input("How many passwords do you want to generate?: "))
    length = int(input("What password length do you want to get?: "))

    print(Fore.GREEN + "Your password has been generated! Result:")
    print(Fore.WHITE)
    for n in range(number):
        password = ''
        for i in range(length):
            password += random.choice(chars)
        print(password)

elif language == "2":
    number = int(input("Сколько паролей вы хотите сгенирировать?: "))
    length = int(input("Какую длину пароля вы хотите получить?: "))

    print(Fore.GREEN + "Ваш пароль сгенерирован! Результат:")
    print(Fore.WHITE)
    for n in range(number):
        password = ''
        for i in range(length):
            password += random.choice(chars)
        print(password)
else:
    print(Fore.RED + "Incorrect language!")

input()