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
    

def color_code(color):
    return return_color_codes()[color]

def colors():
    return [k for k in return_color_codes()]


print(color_code('yellow'))
print(colors())