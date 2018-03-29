"""This isn't a problem in the book but is presented in the chapter notes.
I wanted to take a quick pass at it for practice."""

def fibonacci(n):
    """Return the nth number of the fibonacci sequence (starting at 1).
    Each number in the sequence is the sum of the two previous numbers."""
    if n < 1:
        return None
    p1, p2 = 0, 1
    for num in range(2, n):  # Starting at 2 leaves f(1) = 1 and f(2) = 1
        p1, p2 = p2, p1 + p2
    return p1 + p2

if __name__ == "__main__":
    for x in range(1, 11):
        print('F({}) = {}'.format(x, fibonacci(x)))

