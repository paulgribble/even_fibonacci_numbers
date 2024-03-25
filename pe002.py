fib_1   = 1
fib_2   = 2
f       = fib_1 + fib_2
the_sum = 2
i       = 2
while (f <= 4000000):
    if ((f % 2) == 0):
        the_sum = the_sum + f
    fib_1 = fib_2
    fib_2 = f
    f     = fib_1 + fib_2

print(f"the sum of the even-valued terms is {the_sum}")
