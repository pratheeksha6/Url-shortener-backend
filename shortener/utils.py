#import random
#import string

#def generate_short_code(length=7):
#    characters = string.ascii_letters + string.digits
#    return ''.join(random.choices(characters, k=length))


import string
from .models import Counter

CHARACTERS = string.ascii_letters + string.digits

def get_next_counter():
    counter, created = Counter.objects.get_or_create(id=1)
    counter.value +=1
    counter.save()
    return counter.value

def encode_base62(num):
    if num == 0:
        return CHARACTERS[0]
    result = []
    while num > 0:
        result.append(CHARACTERS[num % 62])
        num //= 62
        code = ''.join(reversed(result))
        return code.rjust(7,CHARACTERS[0])

def generate_short_code():
    num = get_next_counter()
    return encode_base62(num)