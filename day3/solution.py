from collections import Counter

claims = {}


def get_claimed_squares(claim):
    x, y = claim['offset']
    w, h = claim['size']
    return [(x + dx, y + dy) for dx in range(w) for dy in range(h)]


#  claim = {'offset': (3, 2), 'size': (5, 4)}


def part1():
    with open('input') as f:
        #  with open('input_small') as f:
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
        claims_counter.update(claimed_squares)

    print(len([square for square, count
               in claims_counter.items() if count > 1]))


def part2():
    with open('input') as f:
    #  with open('input_small') as f:
        lines = f.readlines()
    squares = {(x, y): set() for x in range(1000) for y in range(1000)}
    #  squares = {(x, y): set() for x in range(7) for y in range(7)}
    claims = {}
    for line in lines:
        line = line.strip()
        tokens = line.split()
        claim_id, _, offset, size = tokens

        claim_id = int(claim_id[1:])
        offset = tuple(map(int, offset[:-1].split(',')))
        size = tuple(map(int, size.split('x')))
        claim = {'offset': offset, 'size': size}
        claimed_squares = get_claimed_squares(claim)
        claims[claim_id] = claimed_squares
        for square in claimed_squares:
            squares[square].add(claim_id)
    #  print(claims)
    #  print('___')
    #  print(squares)
    for claim_id, claimed_squares in claims.items():
        print(f'trying claim #{claim_id}')
        for claimed_square in claimed_squares:
            if len(squares[claimed_square]) != 1:
                break
        else:
            print(claim_id)


part2()
