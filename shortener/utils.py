import random
import string

CHARACTERS = string.ascii_letters + string.digits

def generate_short_code():
    from .models import Url
    while True:
        code = ''.join(random.choices(CHARACTERS, k=7))
        if not Url.objects.filter(short_code=code).exists():
            return code


