# PassGen (v.1.5) by GrobranGG
import random
import colorama
import os
import sys

def convert():
    opersystem = sys.platform

    clean_command = ""
    if sys.platform == "win32":
        clean_command = "cls"
    elif sys.platform == "linux":
        clean_command = "clear"
    os.system(clean_command)

    from colorama import Fore
    colorama.init()

    # Banner
    print(Fore.GREEN + " _____               _____            ")
    print(Fore.GREEN + "|  __ \             / ____|           ")
    print(Fore.GREEN + "| |__) |_ _ ___ ___| |  __  ___ _ __  ")
    print(Fore.GREEN + "|  ___/ _` / __/ __| | |_ |/ _ \ '_ \ ")
    print(Fore.GREEN + "| |  | (_| \__ \__ \ |__| |  __/ | | |")
    print(Fore.GREEN + "|_|   \__,_|___/___/\_____|\___|_| |_|")
    print(Fore.RED + "                  v.1.5 (by GrobranGG)\n")

    # Choose a language
    print(Fore.WHITE + "Choose a language (number):")
    print("1. English")
    print("2. Russian")

    print(Fore.CYAN)
    language = input("Enter your language: ")

    english = {'how many passwords': 'How many passwords do you want to generate?: ', 'length': 'What password length do you want to get?: ', 'generated': 'Your passwords are generated! Result:', 'repeat_question': 'Choose the next action:', 'repeat_variant1': '1. Restart the program',
               'repeat_variant2': '2. Close the program', 'answer_repeat': 'Choose the answer (number): '}
    russian = {'how many passwords': 'Сколько паролей вы хотите сгенирировать?: ', 'length': 'Какую длину пароля вы хотите получить?: ', 'generated': 'Ваши пароли сгенерированы! Результат:', 'repeat_question': 'Выберите следующее действие:', 'repeat_variant1': '1. Переапустить программу',
               'repeat_variant2': '2. Закрыть программу', 'answer_repeat': 'Выбери ответ (число): '}
    if language == "1":
        lang = english
    elif language == "2":
        lang = russian
    else:
        print(Fore.RED + "Incorrect language!")
        input()
        sys.exit()

    chars = '+-/*!&$#?=@<>abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'

    # Password generation
    number = int(input(lang['how many passwords']))
    length = int(input(lang['length']))

    os.system(clean_command)

    print(Fore.GREEN)
    print(lang['generated'])
    print(Fore.WHITE)
    for n in range(number):
        password = ''
        for i in range(length):
            password += random.choice(chars)
        print(password)

    print("\n")
    print(Fore.CYAN + lang['repeat_question'])
    print(Fore.GREEN + lang['repeat_variant1'])
    print(Fore.GREEN + lang['repeat_variant2'])
    repeat = int(input(Fore.WHITE + lang['answer_repeat']))

    if repeat == 1:
        convert()
    if repeat == 2:
        sys.exit()
convert()