def factorize(num):
    """
    given an integer, return the factorial
    """
    processed = 0
    running_total =1 
    current = num
    for x in range(1,num+1):
        running_total *= current
        current -= 1
    processed = running_total
    return processed


if __name__ == '__main__':
    factorize(input())