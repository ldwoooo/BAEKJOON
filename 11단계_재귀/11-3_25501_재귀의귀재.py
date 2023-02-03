def recursion(s, l, r, c):

    c += 1

    if l >= r:  
        return 1, c

    elif s[l] != s[r]:
        return 0, c

    else: 
        return recursion(s, l+1, r-1, c)

def isPalindrome(s):
    c = 0
    return recursion(s, 0, len(s)-1, c)

print(*isPalindrome('AAA'))
print(*isPalindrome('ABBA'))
print(*isPalindrome('ABABA'))
print(*isPalindrome('ABCA'))
print(*isPalindrome('PALINDROME'))
