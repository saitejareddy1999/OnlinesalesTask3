# there is no error, but however if end user gives a input string, we
# have wrap it in try and catch blocks
def compute(n):
    if n < 10:
        out = n ** 2
    elif n < 20:
        out = 1
        for i in range(1, n - 10):
            out *= i
    else:
        lim = n - 20
        out = lim * lim
        out = out - lim
        out = out / 2
    print(out)


try:
    n = int(input("Enter an integer: "))
    compute(n)
except ValueError:
    print("Please enter a valid integer.")
