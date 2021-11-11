import re


def calculating(time_):
     time = re.split('[.,: ]', time_)
     return f'{str(int(time[0]) - 9)}:{time[1]}'


print(calculating(input()))