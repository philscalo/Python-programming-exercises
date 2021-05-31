def sevn_not_five(lowr, uppr):
    """
    Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
    between 2000 and 3200 (both included).

    The numbers obtained should be printed in a comma-separated sequence on a single line.
"""

    listx = [*range(lowr, uppr + 1, 7)]
    listy = list(filter(lambda number: number % 5 != 0, listx))
    return_str = ", ".join(str(num) for num in listy)
    print(return_str)
    return return_str
#[print(','.join(number)) for number in listx if number % 5 != 0]

if __name__ == '__main__':
    sevn_not_five(2000, 3200)