import random
import string
url_map={}
def generate_key(length=6):
    characters=string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))
def shorten_url(long_url):
    key=generate_key()
    while key in url_map:
        key=generate_key()
    url_map[key]=long_url
    return key
def get_Original_url(short_key):
    return url_map.get(short_key,"URL not found")