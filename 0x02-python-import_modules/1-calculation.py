from calculator_1 import add, sub, mul, div
if __name__ == '__main__':
    a = 10
    b = 5
    print('{} + {} = {}'.format(a, b, add(a, b)))
    print('{} - {} = {}'.format(a, b, min(a, b)))
    print('{} * {} = {}'.format(a, b, mul(a, b)))
    print('{} / {} = {}'.format(a, b, div(a, b)))
