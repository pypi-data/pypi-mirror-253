import pyautogui as pag
from time import sleep


def spam(*, message: str, spam_amount: float | int = 5, sets: float | int = 1) -> None:
    if type(spam_amount) == float or type(spam_amount) == int:
        if type(sets) == float or type(sets) == int:
            if type(sets) == float:
                sets = int(sets)
            for set in range(sets):
                if type(spam_amount) == float:
                    spam_amount = int(spam_amount)

                mchars = []

                sleep(7)

                for char in message:
                    mchars.append(char)
                for _ in range(0, spam_amount):
                    for letter in mchars:
                        pag.press(letter)
                    pag.press(pag.KEY_NAMES[pag.KEY_NAMES.index("enter")])
    else:
        raise ValueError(f"{spam_amount} is not a valid integer value.")
