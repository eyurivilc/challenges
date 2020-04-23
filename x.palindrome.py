def palindrome(string):
    from re import sub
    s = sub('[\W_]', '', string.lower())
    print (s == s[::-1])


palindrome('01 01 10 10') 