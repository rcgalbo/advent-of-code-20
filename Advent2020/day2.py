# rcgalbo ~ day 2

import re

EXX = '''1-3 a: abcde
1-3 b: cdefg
2-9 c: ccccccccc'''

with open('data/day2.txt') as f:
    inputs = f.read()

def parse_input(inString):

    policies = inString.split('\n')
    times = []
    letters = []
    passwords = []
    for policy in policies:
        time, letter, password = policy.split(' ')
        letter = letter.replace(':','')
        times.append([int(i) for i in time.split('-')])
        letters.append(letter)
        passwords.append(password)
    
    return passwords, times, letters

passwords, times, letters = parse_input(inputs)

def checkPassword(password, time, letter):

    times = len([l.start() for l in re.finditer(letter, password)])

    if times >= time[0] and times <= time[1]:
        return True
    else:
        return False

correct = sum(checkPassword(p,t,l) for p,t,l in zip(passwords,times,letters))

print(correct)