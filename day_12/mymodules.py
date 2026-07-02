# MODULES
import string
import random

def random_user_id():
    options = string.digits + string.ascii_lowercase
    user_id = ''
    for i in range(6):
        user_id += random.choice(options)
    return user_id

def user_id_gen_by_user():
    options = string.digits + string.ascii_lowercase
    user_id = ''
    length = int(input('Enter user length: '))
    amt = int(input('Enter user generations: '))
    ids = list()
    for j in range(amt):
        for i in range(length):
            user_id += random.choice(options)
        ids.append(user_id)
    return ids

def rgb_color_gen():
    color = 'rgb('
    selected = list()
    for i in range(3):
        selected.append(str(random.randint(0, 255)))
    color += ','.join(selected) + ')'
    return color

def list_of_hexa_colors(count):
    options = string.ascii_lowercase[:6] + string.digits[:10]
    colors = list()
    for j in range(count):
        color = '#'
        for i in range(6):
            color += random.choice(options)
        colors.append(color)
    return colors

def list_of_rgb_colors(count):
    
    return colors
