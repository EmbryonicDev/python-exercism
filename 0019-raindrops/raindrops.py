def convert(number):
    answer = ""
    if number % 3 == 0:
        answer += "Pling"
    if number % 5 == 0:
        answer += "Plang"
    if number % 7 == 0:
        answer += "Plong"
    if answer == "":
        answer = str(number)
    return answer


print(convert(28))
print(convert(30))
print(convert(34))
