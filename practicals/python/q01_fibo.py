''' A program to calculate the n-th term of Fibonacci series using function.
'''


def fibo(n: int, memo: dict = {}) -> int:
    ''' The name 'Fibonacci' is due to a 13th-century Italian mathematician 
    Leonardo of Pisa, who later came to be known as Fibonacci. 
    However, what we popularly call 'Fibonacci numbers' find their earliest mention in the 2nd century BCE work of Acharya Pingala.

    By definition,the 0-th term of the series is zero, and the 1-st term is 1. 
    Any other term is the sum of previous two terms.

    This function uses the concept of memoization to decrease time complexity 
    and increase speed.

    Returns the n-th term of fibbonaci series. Returns -1 for invalid input.

    Args:
        n (int): the term

    Returns:
        int: the nth fibonacci number
    '''
    if n in memo:
        return memo[n]

    if n < 0:
        print(f'Invalid Input \n{fibo.__doc__}')
        raise ValueError('You cannot calculate fibonacci number for n < 0')

    if n <= 2:
        return 1

    memo[n] = fibo(n-1, memo) + fibo(n-2, memo)

    return memo[n]


if __name__ == "__main__":
    # Testing whether the function works correctly

    assert fibo(1) == 1
    assert fibo(2) == 1
    assert fibo(10) == 55
    assert fibo(20) == 6765
    print(f'The 50th fibonacci number is {fibo(50)}')
    print(f'The 100th fibonacci number is {fibo(100)}')
