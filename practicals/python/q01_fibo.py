''' A program to calculate the n-th term of Fibonacci series using function.
'''


def fibo(n: int) -> int:
    ''' The name 'Fibonacci' is due to a 13th-century Italian mathematician Leonardo of Pisa, who later came to be known as Fibonacci. However, what we Indians popularly call 'Fibonacci numbers' find their earliest mention in the 2nd century BCE work of Acharya Pingala.

    By definition,the 0-th term of the series is zero, and the 1-st term is 1. 
    Any other term is the sum of previous two terms.

    Returns the n-th term of fibbonaci series. Returns -1 for invalid input.

    Args:
        n (int): the term

    Returns:
        int: the nth fibonacci number
    '''

    if n < 0:
        print(f'Invalid Input \n{fibo.__doc__}')
        return -1
    if n == 0:
        return 0
    if n == 1:
        return 1

    return fibo(n-1) + fibo(n-2)


if __name__ == "__main__":
    # Testing whether the function works correctly

    assert fibo(0) == 0
    assert fibo(1) == 1
    assert fibo(2) == 1
    assert fibo(10) == 55
    assert fibo(20) == 6765
