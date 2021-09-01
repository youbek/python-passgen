import random
from string import ascii_letters, digits, punctuation

MIN_LENGTH = 6
MAX_LENGTH = 32


def create_password(length=10, no_numbers=False, no_symbols=False):
    # is a string of possible characters for password
    chars_pool = ascii_letters

    # if numbers are allowed, then add list of number chars
    # to possbile characters for password
    if no_numbers == False:
        chars_pool += digits

    # if symbols are allowed, then add list of punctuation chars
    # to possible characters for password
    if no_symbols == False:
        chars_pool += punctuation

    if length < MIN_LENGTH or length > MAX_LENGTH:
        raise RuntimeError(
            f"length must be minimum {MIN_LENGTH} and maximum {MAX_LENGTH}")

    password = "".join(random.choices(chars_pool, k=length))

    return password
