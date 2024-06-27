import sys

read = sys.stdin.readline


def check(max_h):
    return all(land == max_h
               for row in land_map
               for land in row)


def get_max_height():
    return max(map(max, land_map))


def get_required_block(max_h):
    require_block, num = 0, 0
    for row in land_map:
        for land in row:
            if land < max_h:
                require_block += max_h - land
                num += 1
    return require_block, num


n, m, b = map(int, read().split())
land_map = [list(map(int, read().split())) for _ in range(n)]
t, h = 0, 0
