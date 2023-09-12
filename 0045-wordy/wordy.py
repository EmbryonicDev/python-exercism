import string


def get_u_error():
    raise ValueError("unknown operation")


def get_s_error():
    raise ValueError("syntax error")


def calculator(current_answer, num, operator):
    operations = {
        "plus": lambda x, y: x + y,
        "minus": lambda x, y: x - y,
        "multiplied": lambda x, y: x * y,
        "divided": lambda x, y: x / y,
    }
    return operations[operator](current_answer, num)


def answer(question):
    actions = [
        "plus",
        "minus",
        "multiplied",
        "divided",
    ]
    non_actions = "cubed"

    if question == "What is?":
        get_s_error()

    # remove "?"
    question = question.replace("?", "")

    # create list with all words in question
    q_list = question.split(" ")

    calc_instructions = []
    number_count = 0

    for word in q_list:
        # get positive digit
        if word.isdigit():
            calc_instructions.append(int(word))
            number_count += 1
        # get negative digit
        if word[0] == "-":
            calc_instructions.append((int(word[1:])) * -1)
            number_count += 1
        # get actions
        if word in actions:
            calc_instructions.append(word)
        # get non actions
        if word in non_actions:
            get_u_error()

    # error handling
    # if the question is malformed or invalid.
    for i, item in enumerate(calc_instructions):
        # if even item / first item is a number
        if i == 0 or i % 2 == 0:
            try:
                999 + item
            except TypeError:
                get_s_error()
        # if odd item / not first item is not in actions
        if i % 2 != 0 and i != 0 and item not in actions:
            get_s_error()

    # unknown operation if q_list_extract is empty
    if not calc_instructions:
        get_u_error()

    # What is [num]?
    if len(calc_instructions) == 1 and number_count == 1:
        return calc_instructions[0]

    # error handling
    # incompatible qty of operators vs numbers
    if len(calc_instructions) % 2 == 0:
        get_s_error()

    # calculate
    # keep updating final answer & popping q_list_extract
    final_answer = calc_instructions.pop(0)
    while calc_instructions:
        final_answer = calculator(
            final_answer, calc_instructions.pop(1), calc_instructions.pop(0)
        )

    return final_answer


if __name__ == "__main__":
    print(answer("What is 5?"), 5)

    print(answer("What is 1 plus 1?"), 2)

    print(answer("What is 53 plus 2?"), 55)

    print(answer("What is -1 plus -10?"), -11)

    print(answer("What is 123 plus 45678?"), 45801)

    print(answer("What is 4 minus -12?"), 16)

    print(answer("What is -3 multiplied by 25?"), -75)

    print(answer("What is 33 divided by -3?"), -11)

    print(answer("What is 1 plus 1 plus 1?"), 3)

    print(answer("What is 1 plus 5 minus -2?"), 8)

    print(answer("What is 20 minus 4 minus 13?"), 3)

    print(answer("What is 17 minus 6 plus 3?"), 14)

    print(answer("What is 2 multiplied by -2 multiplied by 3?"), -12)

    print(answer("What is -3 plus 7 multiplied by -2?"), -8)

    print(answer("What is -12 divided by 2 divided by -3?"), 2)

    # print(answer("What is 52 cubed?"))

    # print(answer("Who is the President of the United States?"))

    # print(answer("What is 1 2 plus?"))
