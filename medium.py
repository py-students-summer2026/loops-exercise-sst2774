def one(full_list):
    '''this function finds the largest value using a loop'''
    largest = full_list[0]

    for number in full_list:
        if number > largest:
            largest = number

    return largest

def two(full_list):
    '''this function calculates the average of a list using a while loop'''
    total = 0
    i = 0

    while i < len(full_list):
        total += full_list[i]
        i += 1

    return total / len(full_list)

def three(word):
    '''this function checks if a word is a palindrome using a for loop'''
    for i in range(len(word) // 2):
        if word[i] != word[len(word) - 1 - i]:
            return False
    return True

def four(first, ratio, n):
    '''this function prints the first n terms of a geometric sequence using a while loop'''
    term = first

    count = 0

    while count < n:
        print(term)
        term = term * ratio
        count = count + 1

def five(full_list):
    '''finds the second largest and largest number in a list.'''
    largest = full_list[0]

    for number in full_list:
        if number > largest:
            largest = number

    second_largest = full_list[0]

    for number in full_list:
        if number != largest:
            second_largest = number

    for number in full_list:
        if number != largest and number > second_largest:
            second_largest = number

    return second_largest

def six(number):
    '''finds the factorial of a given number.'''
    factorial = 1

    while number > 0:
        factorial = factorial * number
        number = number - 1

    return factorial

def seven(number):
    '''checks for perfect squares.'''
    for i in range(number + 1):
        if i * i == number:
            return True
        if i * i > number:
            return False
    return False

def eight():
    '''sum of all prime numbers.'''
    total = 0
    number = 2

    while number <= 100:
        is_prime = True
        divisor = 2

        while divisor < number:
            if number % divisor == 0:
                is_prime = False
            divisor += 1

        if is_prime:
            total += number

        number += 1

    return total

def nine(sentence):
    '''counts the number of words in a sentence.'''
    for punctuation in [",", ".", "!", "?"]:
        sentence = sentence.replace(punctuation, " ")

    words = sentence.split()

    count = 0

    for word in words:
        if word != "":
            count += 1

    return count

def ten(list_one, list_two):
    '''prints the common elements between two lists.'''
    common = []
    i = 0

    while i < len(list_one):
        if list_one[i] in list_two and list_one[i] not in common:
            common.append(list_one[i])

        i += 1

    return common