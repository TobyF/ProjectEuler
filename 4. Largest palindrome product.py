# Find the largest palindrome made from the product of two 3-digit numbers.

def isPalindrome(S):
    check = len(S) // 2
    for i in range(check + 1):
        if S[i - 1] != S[-i]:
            return False
    return True


def largestPalindrome(n):
    pdromes = []
    for a in range(10 ** (n - 1), 10 ** n):
        for b in range(10 ** (n - 1), 10 ** n):
            x = a * b
            if isPalindrome(str(x)):
                pdromes.append(x)
    print(max(pdromes))


largestPalindrome(3)
