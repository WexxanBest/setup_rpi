import os
from typing import Union


def ask_question(question: str, default_answer: str = None) -> bool:
    tip = f"[default is {default_answer.lower()}]" if default_answer else "[y/n]"
    print(question + ' ' + tip)
    while True:
        user_answer = input('Answer: ').lower().strip()
        if user_answer:
            if user_answer in ('y', 'n', 'yes', 'no'):
                return user_answer in ('y', 'yes')
            else:
                print("Wrong answer! Should be 'y' or 'n'! Try again!")
        else:
            if default_answer:
                return default_answer in ('y', 'yes')
            else:
                print("No answer provided and no default answer, so you should say 'yes' or 'no'!")



def prompt_user(question: str, default_answer: str = None) -> Union[None, str]:
    tip = f" [default is '{default_answer}']" if default_answer else ""
    print(question + ' ' + tip)
    while True:
        user_answer = input('Answer: ')
        if user_answer:
            return user_answer
        else:
            if default_answer:
                return default_answer
            else:
                print("No answer provided and no default answer!")


def check_for_root():
    if os.geteuid() != 0:
        exit("You have to run script with root privileges.\nPlease try again, this time using 'sudo'. Exiting...")