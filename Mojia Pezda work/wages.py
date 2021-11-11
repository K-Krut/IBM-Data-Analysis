import re

EXCHANGE_RATE = 26.26


def converting(bablo):
    babki = re.split('[.,c]', bablo)
    time = float(babki[1]) * 60 / 9
    hours = int(time // 60)
    min = int(time - hours * 60)
    return f'{babki[1]}$ --> {float(babki[1]) * EXCHANGE_RATE}UAH --> {hours}.{min}'


def calculating(time_):
    try:
        time = re.split('[.,: ]', time_)
        wages = (int(time[0]) * 60 + int(time[1])) * 9 / 60 if time[1] else int(time[0]) * 9
    except IndexError:
        wages = int(time_) * 9
    return f'{time_} --> {wages}$ --> {round(wages * EXCHANGE_RATE, 2)}UAH'


def dream(time_):
    try:
        time = re.split('[.,: d]', time_)
        wages = (int(time[1]) * 60 + int(time[1])) * 15 / 60 if time[2] else int(time[1]) * 15
    except IndexError:
        wages = int(time_) * 15
    return f'{time_} --> {wages}$ --> {round(wages * EXCHANGE_RATE, 2)}UAH'


choice = input()

if choice[0] == 'c':
    print(converting(choice))
elif choice[0] == 'd':
    print(dream(choice))
else:
    print(calculating(choice))
