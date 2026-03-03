"""
1456. Maximum Number of Vowels in a Substring of Given Length

You need the maximum count of vowels in any substring of length k.

This is classic sliding window:

Count vowels in the first window of size k

Slide right by 1:

add 1 if the new char is a vowel

subtract 1 if the removed char was a vowel

Track max

Time: O(n)
Space: O(1)
"""

def maxVowels(self, s: str, k: int) -> int:
    vowels = set("aeiou")

    # initial window
    curr = sum(1 for c in s[:k] if c in vowels)
    best = curr

    # slide
    for i in range(k, len(s)):
        if s[i] in vowels:
            curr += 1
        if s[i - k] in vowels:
            curr -= 1
        if curr > best:
            best = curr
            if best == k:  # can't do better than k
                return k

    return best
