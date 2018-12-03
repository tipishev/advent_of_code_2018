from collections import Counter


def part_1():
    doubles = 0
    triples = 0
    with open('day_2_input', 'r') as f:
        for line in f.readlines():
            line = line.strip()
            counter = Counter(line)
            counts = set(counter.values())
            if 2 in counts:
                doubles += 1
            if 3 in counts:
                triples += 1
    result = doubles * triples
    print(f'{doubles}x{triples}={result}')


def distance(one_word, another_word):
    distance = 0
    for one_letter, another_letter in zip(one_word, another_word):
        if one_letter != another_letter:
            distance += 1
    return distance


def part_2():
    words = []
    with open('day_2_input', 'r') as f:
        for line in f.readlines():
            word = line.strip()
            words.append(word)
    combinations = {tuple(sorted([w1, w2]))
                    for w1 in words for w2 in words}
    results = [(w1, w2, set(w1).intersection(set(w2))) for w1, w2 in combinations
               if distance(w1, w2) == 1]
    result = results.pop()
    print(result)


part_2()
