def longestPalindrome(s: str) -> str:
    if not s or len(s) < 1:
        return ""

    start = 0
    max_len = 1 # Single character is always a palindrome

    def expand_around_center(l, r):
        nonlocal start, max_len
        while l >= 0 and r < len(s) and s[l] == s[r]:
            if r - l + 1 > max_len:
                max_len = r - l + 1
                start = l
            l -= 1
            r += 1

    for i in range(len(s)):
        # Odd length palindromes
        expand_around_center(i, i)
        # Even length palindromes
        expand_around_center(i, i + 1)

    return s[start : start + max_len]

print(longestPalindrome("babad"))
print(longestPalindrome("racecartest"))
print(longestPalindrome("cbbd"))