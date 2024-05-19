LEFT = (-1, 0)

def sol():
    def func():
        nonlocal dir
        if dir == LEFT:
            dir = (1, 0)
    dir = (-1, 0)
    func()
    print(dir)
    
sol()