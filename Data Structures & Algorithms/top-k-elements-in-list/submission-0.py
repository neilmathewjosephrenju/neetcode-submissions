import operator
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}

        # Count frequencies
        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1

        # Sort by frequency in descending order
        sorted_nums = sorted(
            freq.items(),
            key=operator.itemgetter(1),
            reverse=True
        )

        # Return only the first k numbers
        return [num for num, count in sorted_nums[:k]]