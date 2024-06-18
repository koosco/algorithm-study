import sys
read = sys.stdin.readline

while True:
    try:
        A, B = map(int, read().split())
        print(A+B)
    except:
        break