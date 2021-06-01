def square_dict(num):
    results = dict(zip([x for x in range(1, int(num) + 1)], [x*x for x in range(1, int(num) + 1)]))
    return results


if __name__ == '__main__':
    square_dict(input())