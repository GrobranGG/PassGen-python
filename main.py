# PassGen (v.1.3) by GrobranGG
import random
import colorama
import os
import sys

opersystem = sys.platform

if opersystem == "win32":
    os.system("cls")
elif opersystem == 'linux':
    os.system("clear")

from colorama import Fore
colorama.init()

# Banner
print(Fore.GREEN + " _____               _____            ")
print(Fore.GREEN + "|  __ \             / ____|           ")
print(Fore.GREEN + "| |__) |_ _ ___ ___| |  __  ___ _ __  ")
print(Fore.GREEN + "|  ___/ _` / __/ __| | |_ |/ _ \ '_ \ ")
print(Fore.GREEN + "| |  | (_| \__ \__ \ |__| |  __/ | | |")
print(Fore.GREEN + "|_|   \__,_|___/___/\_____|\___|_| |_|")
print(Fore.RED + "                  v.1.3 (by GrobranGG)\n")

# Choose a language
print(Fore.WHITE + "Choose a language (number):")
print("1. English")
print("2. Russian")

print(Fore.CYAN)
language = input("Enter your language: ")

english = {'how many passwords': 'How many passwords do you want to generate?: ', 'length': 'What password length do you want to get?: ', 'generated': 'Your passwords are generated! Result:'}
russian = {'how many passwords': 'Сколько паролей вы хотите сгенирировать?: ', 'length': 'Какую длину пароля вы хотите получить?: ', 'generated': 'Ваши пароли сгенерированы! Результат:'}
if language == "1":
    lang = english
elif language == "2":
    lang = russian
else:
    print(Fore.RED + "Incorrect language!")

chars = '+-/*!&$#?=@<>abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'

# Password generation
number = int(input(lang['how many passwords']))
length = int(input(lang['length']))

if opersystem == "win32":
    os.system("cls")
elif opersystem == 'linux':
    os.system("clear")

print(Fore.GREEN)
print(lang['generated'])
print(Fore.WHITE)
for n in range(number):
    password = ''
    for i in range(length):
        password += random.choice(chars)
    print(password)

input()