import easy
import medium
import difficult

def do_easy():
    # "easy" problems
    easy.one()
    easy.two()
    easy.three()
    easy.four()
    easy.five(10)
    easy.six(8)
    easy.seven('circumlocution')
    easy.eight(24)
    easy.nine()
    easy.ten('circumlocution')
    pass # do nothing

def do_medium():
    # "medium" problems

    print("\nQuestion 1. Largest value of [3, 7, 8, 10, 67, 14]: ")
    print(medium.one([3, 7, 8, 10, 67, 14]))

    print("\nQuestion 2. The average of [1, 4, 5, 6, 10]: ")
    print(medium.two([1, 4, 5, 6, 10]))

    print("\nQuestion 3. Is 'wow' a palindrome? ")
    print(medium.three('wow'))

    print("\nQuestion 4. The first 10 terms of a geometric sequence [2, 3, 10]: ")
    medium.four(2, 3, 10)

    print("\nQuestion 5. The second largest number in [1, 10, 3, 11]: ") 
    print(medium.five([1, 10, 3, 11]))

    print("\nQuestion 6. The factorial of 8: ") 
    print(medium.six(8))

    print("\nQuestion 7. Is 9 a perfect square? ") 
    print(medium.seven(9))

    print("\nQuestion 8. The sum of prime numbers between 1 - 100? ") 
    print(medium.eight())

    print("\nQuestion 9. Number of words in 'Who goes there, sir': ") 
    print(medium.nine('Who goes there, sir'))

    print("\nQuestion 10. What are the common elements between [0, 10, 5, 3] and [10, 0, 9, 8]: ") 
    print(medium.ten([0, 10, 5, 3], [10, 0, 9, 8]))

    pass # do nothing
def do_difficult():
    # "difficult" problems
    print("\nQuestion 1. Prime factors of 60: ")
    print(difficult.one(60))

    print("\nQuestion 2. 10th Fibonacci term: ")
    print(difficult.two(10))

    print("\nQuestion 3. Are 'listen' and 'silent' anagrams? ")
    print(difficult.three("listen", "silent"))

    print("\nQuestion 4. First 5 terms of arithmetic sequence (start 2, difference 3): ")
    difficult.four(2, 3, 5)

    print("\nQuestion 5. Median of [7, 1, 3, 9, 5]: ")
    print(difficult.five([7, 1, 3, 9, 5]))

    print("\nQuestion 6. Is 28 a perfect number? ")
    print(difficult.six(28))

    print("\nQuestion 7. Sum of digits in 12345: ")
    print(difficult.seven(12345))

    print("\nQuestion 8. Longest word in 'The quick brown fox jumped': ")
    print(difficult.eight("The quick brown fox jumped"))

    print("\nQuestion 9. Is 'The quick brown fox jumps over the lazy dog' a pangram? ")
    print(difficult.nine("The quick brown fox jumps over the lazy dog"))

    print("\nQuestion 10. Primes between 1 and 1000: ")
    difficult.ten()
    pass # do nothing

def main():
    do_easy()
    do_medium()
    do_difficult()

main()
