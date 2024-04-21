import random


def get_numbers_ticket(min, max, quantity):
    result = []

    if 1 <= min <= max <= 1000 and quantity <= (max - min):
        result = random.sample(range(min, max + 1), k=quantity)

    return sorted(result)


lottery_numbers = get_numbers_ticket(10, 150, 3)
print("Ваші лотерейні числа:", lottery_numbers)
