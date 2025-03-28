x = float(input('Please enter a number: '))

if 0 <= x <= 1:
    def error(a, b):
        return a ** ((2 * b) + 1) / ((2 * b) + 1)
    n = 0
    while error(x, n) >= 0.0001:
        n += 1
    i = 0
    f = 0
    while i < n:
        term = ((-1) ** i) * (x ** ((2 * i) + 1)) / ((2 * i) + 1)
        f += term
        i += 1
    output = (f, n, error(x, n))
    print(output)
else:
    print('Error!')
