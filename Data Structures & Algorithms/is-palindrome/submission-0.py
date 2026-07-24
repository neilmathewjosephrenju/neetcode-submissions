class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        t = ""
        g=""

        for i in s:
            if i.isalnum():
                g=i+g
        for i in s[::-1]:
            if i.isalnum():
                t = i+t
        return t==g
