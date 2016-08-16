def double_check(string):
    lowString = string.lower()
    for i in range(0, len(lowString)-1):
        if lowString[i] == lowString[i+1]:
            return True
    return False
