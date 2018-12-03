claims = {}

with open('input') as f:
    lines = f.readlines()

for line in lines:
    line = line.strip()
    tokens = line.split()
    claim_id, _, offset, size = tokens

    claim_id = int(claim_id[1:])
    offset = tuple(map(int, offset[:-1].split(',')))
    size = tuple(map(int, size.split('x')))
    claims[claim_id] = {'offset': offset, 'size': size}
    print(claims)
