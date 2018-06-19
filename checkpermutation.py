def checkPermutation(str1, str2):
     # Map characters to prime numbers to multiply
    if len(str1)!= len(str2):
        return False
    
    dict = {}
    for ch in str1:
        if ch not in dict.keys():
            dict[ch]= 1
        else:
            dict[ch]+= 1
    print(dict)
    for ch in str2:
        if ch not in dict.keys():
            return False
        else:
            dict[ch]-=1
            if dict[ch] <0:
                return False
    return True

print(checkPermutation("jasbha", "hsabja"))
