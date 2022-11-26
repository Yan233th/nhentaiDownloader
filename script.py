def IsDigit (text):
    for i in text:
        if i >= "0" and i <= "9":
            continue
        else:
            return False
    return True