def is_armstrong_number(number):
    str_num = str(number)
    num_len = len(str_num)
    check = 0
    
    for num in str_num:
        num = int(num)
        check += num ** num_len
        
    return check == number

    
    
    
print(is_armstrong_number(5))
print(is_armstrong_number(10))
print(is_armstrong_number(153))
print(is_armstrong_number(9474))
print(is_armstrong_number(9475))






