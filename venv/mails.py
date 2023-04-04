from functools import wraps
import random
random.seed(1)
from string import ascii_lowercase, ascii_uppercase
chars = ascii_lowercase + ascii_uppercase + "0123456789!?@#$*"
pass_to_form = '123'
dlina_passw = random.randint(9, 15)
def password():
    def get_pas(func):
        global pass_to_form
        pass_to_form = ''.join(func())
    return get_pas


@password()
def pas_generator():
    for i in range(dlina_passw):
        indx = random.randint(0, len(chars) - 1)
        yield chars[indx]


print(pass_to_form)