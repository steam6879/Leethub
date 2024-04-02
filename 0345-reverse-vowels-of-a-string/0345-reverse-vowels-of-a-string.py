class Solution:
    def reverseVowels(self, s: str) -> str:
        m = {'a', 'e', 'i', 'o', 'u'}
        vowels = []
        s = list(s)

        for char in s:
            if char.lower() in m:
                vowels.append(char)

        for i in range(len(s)):
            if s[i].lower() in m:
                s[i] = vowels.pop()

        return ''.join(s)