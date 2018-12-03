from itertools import cycle
with open('day_1_input.txt') as f:
    numbers = cycle([int(l.strip()) for l in f.readlines()])
    frequencies = set()
    frequency = 0
    for number in numbers:
        frequency += number
        if frequency in frequencies:
            print(frequency)
            break
        frequencies.add(frequency)
