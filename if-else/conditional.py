import random

def is_positive(num):
    if num >= 0:
        return True
    else:
        return False
    # return true if num is positive, otherwise return false

def is_even(num):
    # return true if num is even, otherwise return false
    if num % 2 == 0:
        return True
    else:
        return False


def is_positive_and_even(num):
    # return true if num is positive and even, otherwise return false
    if num % 2 == 0 and num >= 0:
        return True
    else:
        return False


def is_positive_or_even(num):
    # return true if num is positive or even, otherwise return false
    if num % 2 == 0 or num >= 0:
        return True
    else:
        return False

print(is_positive(random.randint(-30,30)))
print(is_even(random.randint(-30,30)))
print(is_positive_and_even(random.randint(-30,30)))
print(is_positive_or_even(random.randint(-30,30)))
