def sol(y: int):
    if y % 100 == 0 and y % 400 != 0:
        return False
    if y % 4 == 0:
        return True
    return False
    
y = int(input())
print('true' if sol(y) else 'false')