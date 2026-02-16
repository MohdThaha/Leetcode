class Solution:
    def firstUniqueFreq(self, nums: List[int]) -> int:
        freq = Counter(nums)                 # number -> frequency
        freq_count = Counter(freq.values())  # frequency -> how many numbers have it

        for n in nums:
            if freq_count[freq[n]] == 1:
                return n

        return -1