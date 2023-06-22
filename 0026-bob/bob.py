import re

def response(remark):
    remark = remark.strip()
    if remark == "":
        return "Fine. Be that way!"
    if remark.isupper() and re.search(r'[A-Z]', remark):
        if remark.endswith("?"):
            return "Calm down, I know what I'm doing!"
        else:
            return "Whoa, chill out!"
    if remark.endswith("?"):
        return "Sure."
    return "Whatever."
    
print(response("Does this cryogenic chamber make me look fat?"))
print(response("FCECDF!CAAB"))
print(response("WHAT'S GOING ON?"))
print(response('hello'))
print(response(''))
print(response('   '))
print(response("1, 2, 3"))

    
