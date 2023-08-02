def is_isogram(string):
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    word_check = ''
    for l in string:
        l_lower = l.lower()
        if l_lower in word_check:
            return False
        if l_lower in alpha:
            word_check += l_lower
    return True
    
    
print(is_isogram('lumberjacks'))
print(is_isogram('lumberjackss'))
print(is_isogram('background'))
print(is_isogram('backgrounnd'))
print(is_isogram('downstream'))
print(is_isogram('downstreamm'))
print(is_isogram('six-year-old'))
print(is_isogram('six-yeear-old'))

