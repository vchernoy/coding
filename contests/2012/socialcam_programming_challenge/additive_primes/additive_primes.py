import math

def prime(num):
    x = 7
    max_x = int(math.sqrt(num))
    while x <= max_x:
        if num % x == 0:
            return False

        x += 4 
        if num % x == 0:
            return False

        x += 2 
        if num % x == 0:
            return False

        x += 4
        if num % x == 0:
            return False

        x += 2
        if num % x == 0:
            return False

        x += 4
        if num % x == 0:
            return False

        x += 6
        if num % x == 0:
            return False

        x += 2
        if num % x == 0:
            return False

        x += 6

    return True

prime_set = set([2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79])
    
steps = [4,2,4,2,4,6,2,6]

n = int(raw_input())

if n == 1:
    print 2
elif n == 2:
    print 3
elif n == 3:
    print 5
elif n == 4:
    print 7
else:
    no_step = 0
    i = 4
    num = 7
    while True:
        m = num
        digit_sum = 0
        while m > 0:
            digit_sum += m % 10
            m /= 10

        if (digit_sum in prime_set) and prime(num):
            i += 1
            if i > n:
                break

        num += steps[no_step]
        no_step = (no_step + 1) % 8

    print num

