from collections import Counter

claims = {}


def get_claimed_squares(claim):
    x, y = claim['offset']
    w, h = claim['size']
    return [(x + dx, y + dy) for dx in range(w) for dy in range(h)]


#  claim = {'offset': (3, 2), 'size': (5, 4)}


def run():
    #  with open('input') as f:
    with open('input_small') as f:
        lines = f.readlines()

    claims_counter = Counter()
    for line in lines:
        line = line.strip()
        tokens = line.split()
        claim_id, _, offset, size = tokens

        claim_id = int(claim_id[1:])
        offset = tuple(map(int, offset[:-1].split(',')))
        size = tuple(map(int, size.split('x')))
        claim = {'offset': offset, 'size': size}
        claims[claim_id] = claim
        claimed_squares = get_claimed_squares(claim)
        print(claimed_squares)
        claims_counter.update(claims_counter)

    print(len([square for square, count in claims_counter if count > 1]))


run()
