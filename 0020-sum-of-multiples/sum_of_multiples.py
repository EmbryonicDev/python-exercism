def sum_of_multiples(limit, multiples):
    my_set = set()

    if len(multiples) < 1:
        return 0

    for num in multiples:
        num_copy = num

        if num == 0:
            continue

        while num_copy < limit:
            my_set.add(num_copy)
            num_copy += num

    return sum(my_set)


COUNT = 1


print()
print("#", COUNT)
COUNT += 1
print(sum_of_multiples(15, [4, 6]))

print()
print("#", COUNT)
COUNT += 1
print(sum_of_multiples(150, [5, 6, 8]))

print()
print("#", COUNT)
COUNT += 1
print(sum_of_multiples(51, [5, 25]))

print()
print("#", COUNT)
COUNT += 1
print(sum_of_multiples(10000, [43, 47]))

print()
print("#", COUNT)
COUNT += 1
print(sum_of_multiples(100, [1]))

print()
print("#", COUNT)
COUNT += 1
print(sum_of_multiples(10000, []))

print()
print("#", COUNT)
COUNT += 1
print(sum_of_multiples(1, [0]))

print()
print("#", COUNT)
COUNT += 1
print(sum_of_multiples(4, [3, 0]))

print()
print("#", COUNT)
COUNT += 1
print(sum_of_multiples(10, [3, 5]))

print()
print("#", COUNT)
COUNT += 1
print(sum_of_multiples(150, [5, 6, 8]))

print()
print("#", COUNT)
COUNT += 1
print(sum_of_multiples(51, [5, 25]))

print()
print("#", COUNT)
COUNT += 1
print(sum_of_multiples(10000, [43, 47]))

print()
print("#", COUNT)
COUNT += 1
print(sum_of_multiples(100, [1]))

print()
print("#", COUNT)
COUNT += 1
print(sum_of_multiples(10000, []))

print()
print("#", COUNT)
COUNT += 1
print(sum_of_multiples(1, [0]))

print()
print("#", COUNT)
COUNT += 1
print(sum_of_multiples(4, [3, 0]))

print()
print("#", COUNT)
COUNT += 1
print(sum_of_multiples(10000, [2, 3, 5, 7, 11]))
