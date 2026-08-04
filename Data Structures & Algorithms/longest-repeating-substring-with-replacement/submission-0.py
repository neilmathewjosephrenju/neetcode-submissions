class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        left = 0
        maxFreq = 0
        longest = 0

        for right in range(len(s)):
            # Add the current character to the window
            count[s[right]] = 1 + count.get(s[right], 0)

            # Update the highest frequency in the current window
            maxFreq = max(maxFreq, count[s[right]])

            # If the window needs more than k replacements, shrink it
            while (right - left + 1) - maxFreq > k:
                count[s[left]] -= 1
                left += 1

            # Update the longest valid window
            longest = max(longest, right - left + 1)

        return longest