def sliding_window(s: str) -> int:
    left = 0
    state = {}  # or [0]*26
    best = 0

    for right, ch in enumerate(s):
        # add ch to state
        state[ch] = state.get(ch, 0) + 1

        # while window invalid:
        # while condition(state) is False:
        #     state[s[left]] -= 1
        #     if state[s[left]] == 0:
        #         del state[s[left]]
        #     left += 1

        # update best with current window
        best = max(best, right - left + 1)

    return best


def two_pointers(s: str) -> bool:
    l, r = 0, len(s) - 1
    while l < r:
        # optional skip
        # while l < r and not s[l].isalnum(): l += 1
        # while l < r and not s[r].isalnum(): r -= 1

        if s[l] != s[r]:
            return False
        l += 1
        r -= 1
    return True

from collections import Counter

def is_anagram(a: str, b: str) -> bool:
    if len(a) != len(b):
        return False
    return Counter(a) == Counter(b)


def decode_string(s: str) -> str:
    stack = []
    num = 0
    curr = []

    for ch in s:
        if ch.isdigit():
            num = num * 10 + int(ch)
        elif ch == '[':
            stack.append((curr, num))
            curr = []
            num = 0
        elif ch == ']':
            prev, k = stack.pop()
            curr = prev + curr * k
        else:
            curr.append(ch)

    return "".join(curr)

def longest_palindrome(s: str) -> str:
    if not s:
        return ""

    def expand(l: int, r: int) -> tuple[int, int]:
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return l + 1, r - 1

    best_l, best_r = 0, 0
    for i in range(len(s)):
        l1, r1 = expand(i, i)
        l2, r2 = expand(i, i + 1)
        if r1 - l1 > best_r - best_l:
            best_l, best_r = l1, r1
        if r2 - l2 > best_r - best_l:
            best_l, best_r = l2, r2

    return s[best_l:best_r + 1]


class TrieNode:
    __slots__ = ("children", "end")
    def __init__(self):
        self.children = {}
        self.end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for ch in word:
            node = node.children.setdefault(ch, TrieNode())
        node.end = True

    def search(self, word: str) -> bool:
        node = self.root
        for ch in word:
            if ch not in node.children:
                return False
            node = node.children[ch]
        return node.end

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for ch in prefix:
            if ch not in node.children:
                return False
            node = node.children[ch]
        return True

def build_lps(p: str) -> list[int]:
    lps = [0] * len(p)
    j = 0
    for i in range(1, len(p)):
        while j > 0 and p[i] != p[j]:
            j = lps[j - 1]
        if p[i] == p[j]:
            j += 1
            lps[i] = j
    return lps

def kmp_search(s: str, p: str) -> int:
    if p == "":
        return 0
    lps = build_lps(p)
    j = 0
    for i in range(len(s)):
        while j > 0 and s[i] != p[j]:
            j = lps[j - 1]
        if s[i] == p[j]:
            j += 1
            if j == len(p):
                return i - len(p) + 1
    return -1

def lcs(a: str, b: str) -> int:
    n, m = len(a), len(b)
    dp = [0] * (m + 1)

    for i in range(1, n + 1):
        prev_diag = 0
        for j in range(1, m + 1):
            temp = dp[j]
            if a[i - 1] == b[j - 1]:
                dp[j] = prev_diag + 1
            else:
                dp[j] = max(dp[j], dp[j - 1])
            prev_diag = temp

    return dp[m]
