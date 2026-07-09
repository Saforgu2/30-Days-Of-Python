# DAY 18

import re

# LEVEL 1

paragraph = '''I love teaching.
If you do not love teaching what else can you love.
I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love.'''

cleaned = re.findall(r'\b\w+\b', paragraph.lower())
not_repeated = set(cleaned)
counter = list()
highest = (0, '')
for i in not_repeated:
    found = re.findall((i + '[ .]'), paragraph, re.I)
    counter.append((len(found), i))
    if(highest[0] < len(found)):
        highest = (len(found), i)
print(counter)
print(highest)

info = 'The position of some particles on the horizontal x-axis are -12, -4, -3 and -1 in the negative direction, 0 at origin, 4 and 8 in the positive direction.'
pattern = r'[-| ]\d{1,3}'
points = re.findall(pattern, info, re.I)
sorted_points = [int(i) for i in points] # or map(int, points)
print('Distance: ', sorted_points[-1] - sorted_points[0])

# LEVEL 2

variable_name = input('Write a variable name: ')
def is_valid_variable(name):
    pattern = r'^[a-zA-Z_]\w*$'
    is_valid = re.match(pattern, name)
    if(is_valid == None):
        return False
    return True
print(is_valid_variable(variable_name))

# LEVEL 3

sentence = '''%I $am@% a %tea@cher%, &and& I lo%#ve %tea@ching%;. There $is nothing; &as& mo@re rewarding as educa@ting &and& @emp%o@wering peo@ple. ;I found tea@ching m%o@re interesting tha@n any other %jo@bs. %Do@es thi%s mo@tivate yo@u to be a tea@cher!?'''
cleaned_sentence = re.sub('[%$#@&;!?]', '', sentence)
def most_frequent_words(clean_text):
    all_words = re.findall(r'\b[a-zA-Z]+\b', clean_text, re.I)
    print(all_words)
    not_repeated = set(all_words)
    counter = list()
    for i in not_repeated:
        found = re.findall(r'\b' + i + r'\b', clean_text, re.I)
        counter.append((len(found), i))
    for i in range(0, len(counter)):
        for j in range(0, len(counter) - i - 1):
            if(counter[j][0] > counter[j + 1][0]):
                tmp = counter[j]
                counter[j] = counter[j + 1]
                counter[j + 1] = tmp
    return counter[-3:]
print(most_frequent_words(cleaned_sentence))
