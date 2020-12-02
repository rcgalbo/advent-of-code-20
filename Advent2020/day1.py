 # rcgalbo day 1

with open('data/day1.txt') as f:
    EXX = f.read()

def parse_input(inString):

    numbers = [int(i) for i in inString.split('\n')]
    
    for number1 in numbers:
        for number2 in numbers:
            for number3 in numbers:
                if number1+number2+number3 == 2020:
                    return number1 * number2 * number3

print(parse_input(EXX))