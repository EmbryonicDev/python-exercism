def prime(number):
    if number < 1:
        raise ValueError('there is no zeroth prime')

    primes = [2]
    current_num = 3

    while len(primes) < number:
        if all(current_num % num != 0 for num in primes):
            primes.append(current_num)
        current_num += 2  # Skip even numbers (except 2) to improve efficiency

    return primes[-1]
