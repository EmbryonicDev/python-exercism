def square(number):
    if not (1 <= number <= 64):
        raise ValueError("square must be between 1 and 64")
    return 2 ** (number - 1)

def total():
    return 2 ** 64 - 1
        

print(square(1))
print(square(2))
print(square(3))
print(square(8))
print(square(16))

print(total())
print(square(65))





