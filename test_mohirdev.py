

# task_1

import random
def user_name(ism):
    ism = ism.lower()
    new_username = ""
    for item in range(len(ism) - 1, -1, -1):
        new_username += ism[item]
    new_username += str(random.randint(1, 10))
    return new_username


# task 2
def convert_add(listt):
    summ = 0
    while listt:
        summ += int(listt.pop())
    return summ

