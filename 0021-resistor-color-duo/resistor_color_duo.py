def return_color_codes():
    return {
        'black': 0,
        'brown': 1,
        'red': 2,
        'orange': 3,
        'yellow': 4,
        'green': 5,
        'blue': 6,
        'violet': 7,
        'grey': 8,
        'white': 9,
        }

def value(colors: list):
    answer = str(return_color_codes()[colors[0]])
    answer += str(return_color_codes()[colors[1]])
    return int(answer)
    
print(value(['red', 'violet']))
