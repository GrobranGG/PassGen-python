# PassGen (v.1.6) by GrobranGG
import random
import colorama
import os
import sys


def convert():
    clean_command = ""
    if sys.platform == "win32":
        clean_command = "cls"
    elif sys.platform == "linux":
        clean_command = "clear"
    os.system(clean_command)

    from colorama import Fore
    colorama.init()
    
    banner = """
██████   █████  ███████ ███████  ██████  ███████ ███    ██ 
██   ██ ██   ██ ██      ██      ██       ██      ████   ██ 
██████  ███████ ███████ ███████ ██   ███ █████   ██ ██  ██ 
██      ██   ██      ██      ██ ██    ██ ██      ██  ██ ██ 
██      ██   ██ ███████ ███████  ██████  ███████ ██   ████ 
"""
    print(Fore.GREEN + banner)
    print(Fore.RED + "\t\t\t\t\t\t\t\t\t\tv.1.6 (By GrobranGG)\n")

    # Choose a language
    print(Fore.WHITE + "Choose a language (number):")
    print("1. English")
    print("2. Russian")

    language = int(input(Fore.CYAN + "Enter your language: "))

    english = {'how many passwords': 'How many passwords do you want to generate?: ',
               'length': 'Password length?: ',
               'generated': 'Your passwords have been generated! Result:', 'repeat_question': 'Choose the next action:',
               'repeat_variant1': '1. Generate more passwords',
               'repeat_variant2': '2. Exit the program', 'answer_repeat': 'Choose the answer (number): '}
    russian = {'how many passwords': 'Сколько паролей вы хотите сгенирировать?: ',
               'length': 'Какую длину пароля вы хотите получить?: ',
               'generated': 'Ваши пароли сгенерированы! Результат:', 'repeat_question': 'Выберите следующее действие:',
               'repeat_variant1': '1. Переапустить программу',
               'repeat_variant2': '2. Закрыть программу', 'answer_repeat': 'Выбери ответ (число): '}
    if language == 1:
        lang = english
    elif language == 2:
        lang = russian
    else:
        print(Fore.RED + "Invalid language!")
        sys.exit()

    chars = "+-/*!&$#?=@<>'\"abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"  # Symbols to generate

    # Password generation
    number = int(input(lang['how many passwords']))
    length = int(input(lang['length']))
    os.system(clean_command)

    print(Fore.GREEN + lang['generated'])
    for n in range(number):
        password = ''
        for i in range(length):
            password += random.choice(chars)
        print(Fore.WHITE + password)

    print("\n")
    print(Fore.CYAN + lang['repeat_question'])
    print(Fore.GREEN + lang['repeat_variant1'])
    print(lang['repeat_variant2'])
    repeat = input(Fore.WHITE + lang['answer_repeat'])

    if repeat == "1":
        convert()
    if repeat == "2":
        sys.exit()


if __name__ == '__main__':
    convert()
