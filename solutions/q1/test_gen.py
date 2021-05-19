def generate():
    for number in range(2000, 3200, 7):
        yield number


def countdown(n):
    while n > 0:
        yield n
        n -= 1

for x in countdown(15):
    print(f'T-minus {x!s}')

if __name__ == '__main__':
    countdown()