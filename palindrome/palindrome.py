def check_palindrome(str):
    start= 0
    end = len(str)-1
    while start < end:
        if str[start]!= str[end]:
            return False
        start+=1
        end-=1
    return True


print(check_palindrome("abba"))
print(check_palindrome("abcba"))
print(check_palindrome("abcbsa"))