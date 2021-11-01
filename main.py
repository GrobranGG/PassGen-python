# PassGen (v.1.2) by GrobranGG
import random
import colorama
import secrets
import os

os.system("clear")
os.system("cls")
from colorama import init
from colorama import Fore, Back
from random import randint
init()

# Banner
print(Fore.GREEN + " _____               _____            ")
print(Fore.GREEN + "|  __ \             / ____|           ")
print(Fore.GREEN + "| |__) |_ _ ___ ___| |  __  ___ _ __  ")
print(Fore.GREEN + "|  ___/ _` / __/ __| | |_ |/ _ \ '_ \ ")
print(Fore.GREEN + "| |  | (_| \__ \__ \ |__| |  __/ | | |")
print(Fore.GREEN + "|_|   \__,_|___/___/\_____|\___|_| |_|")
print(Fore.RED + "                  v.1.2 (by GrobranGG)\n")

# Choose a language
print(Fore.WHITE + "Choose a language (number):")
print("1. English")
print("2. Russian")

print(Back.RESET)
print(Fore.CYAN)
language = input("Enter your language: ")
chars = '+-/*!&$#?=@<>abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'

# Password generation
if language == "1":
    number = int(input("How many passwords do you want to generate?: "))
    length = int(input("What password length do you want to get?: "))

    os.system("clear")
    os.system("cls")
    print(Fore.GREEN + "Your passwords are generated! Result:")
    print(Fore.WHITE)
    for n in range(number):
        password = ''
        for i in range(length):
            password += random.choice(chars)
        print(password)

elif language == "2":
    number = int(input("Сколько паролей вы хотите сгенирировать?: "))
    length = int(input("Какую длину пароля вы хотите получить?: "))

    os.system("clear")
    os.system("cls")
    print(Fore.GREEN + "Ваши пароли сгенерированы! Результат:")
    print(Fore.WHITE)
    for n in range(number):
        password = ''
        for i in range(length):
            password += random.choice(chars)
        print(password)
else:
    print(Fore.RED + "Incorrect language!")

input()