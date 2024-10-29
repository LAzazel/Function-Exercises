from random import randint, choice
from string import ascii_lowercase, digits
from functools import reduce
from inspect import signature

def my_random(min, max=None):
    if max is None:
        max = min
        min = 0
    return randint(min, max)

def generate_key(length, characters):
    x = ''
    for i in range(length):
        x += choice(characters)
    return x

def ip_to_int(ip='127.0.0.1'):
    res = list(map(int, ip.split('.')))
    return reduce(lambda x, y: (x << 8) + y, res)

iface = {
    'm1': lambda x: [x],
    'm2': lambda x, y: [x, y],
    'm3': lambda x, y, z: [x, y, z],
}

def introspect(obj):
    return [[key, len(signature(value).parameters)] for key, value in obj.items()]


print(my_random(19))
print(generate_key(10, ascii_lowercase + digits))
print(ip_to_int('10.0.0.1'))
print(introspect(iface))