def is_pangram(sentence):
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    alpha_check = ''
    
    for l in sentence:
        lower_l = l.lower()
        if lower_l in alpha and lower_l not in alpha_check:
            alpha_check += lower_l
    if len(alpha_check) != 26:
        return False
    return True
        
print(is_pangram('abcdefghijklmnopqrstuvwxyz'))
print(is_pangram('abcdefghijmnopqrstuvwxyz'))
print(is_pangram('abcdefghijklm ABCDEFGHIJKLM'))

