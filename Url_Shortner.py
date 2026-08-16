import random
import string
url_map={}
def generate_key(length=6):
    characters=string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))
