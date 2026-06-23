def one(number):
    '''this function finds the prime factors of a number using a for loop'''
    factors = []

    for divisor in range(2, number + 1):
        if number % divisor == 0:
            is_prime = True

            for check in range(2, divisor):
                if divisor % check == 0:
                    is_prime = False

            if is_prime:
                factors.append(divisor)

    return factors


def two(n):
    '''this function finds the nth term of the Fibonacci sequence using a while loop'''
    current = 0
    next_number = 1

    count = 0

    while count < n:
        new_number = current + next_number
        current = next_number
        next_number = new_number
        count = count + 1

    return current


def three(first_word, second_word):
    '''this function checks if two words are anagrams using a for loop'''
    first_word = sorted(first_word.replace(" ", "").lower())
    second_word = sorted(second_word.replace(" ", "").lower())

    if len(first_word) != len(second_word):
        return False

    for i in range(len(first_word)):
        if first_word[i] != second_word[i]:
            return False

    return True


def four(first, difference, n):
    '''this function prints the first n terms of an arithmetic sequence using a while loop'''
    term = first

    count = 0

    while count < n:
        print(term)
        term = term + difference
        count = count + 1


def five(full_list):
    '''this function finds the median of a list using a for loop'''
    ordered = list(full_list)

    for i in range(len(ordered)):
        smallest = i

        for j in range(i + 1, len(ordered)):
            if ordered[j] < ordered[smallest]:
                smallest = j

        temp = ordered[i]
        ordered[i] = ordered[smallest]
        ordered[smallest] = temp

    middle = len(ordered) // 2

    if len(ordered) % 2 == 1:
        return ordered[middle]

    return (ordered[middle - 1] + ordered[middle]) / 2


def six(number):
    '''this function checks if a number is a perfect number using a while loop'''
    if number <= 1:
        return False

    total = 0

    divisor = 1

    while divisor < number:
        if number % divisor == 0:
            total = total + divisor
        divisor = divisor + 1

    return total == number


def seven(number):
    '''this function sums all digits in a number using a for loop'''
    total = 0

    for digit in str(abs(number)):
        total = total + int(digit)

    return total


def eight(sentence):
    '''this function finds the longest word in a sentence using a while loop'''
    words = sentence.split()

    longest = ""

    index = 0

    while index < len(words):
        if len(words[index]) > len(longest):
            longest = words[index]
        index = index + 1

    return longest


def nine(sentence):
    '''this function checks if a sentence is a pangram using a for loop'''
    sentence = sentence.lower()

    for letter in "abcdefghijklmnopqrstuvwxyz":
        if letter not in sentence:
            return False

    return True


def ten():
    '''this function prints the prime numbers between 1 and 1000 using a while loop'''
    number = 2

    while number <= 1000:
        is_prime = True

        divisor = 2

        while divisor < number:
            if number % divisor == 0:
                is_prime = False
            divisor = divisor + 1

        if is_prime:
            print(number)

        number = number + 1