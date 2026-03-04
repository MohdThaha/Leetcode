class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque()
        res = []

        for i in range(len(nums)):

            # 1️⃣ Remove elements outside window
            if dq and dq[0] <= i - k:
                dq.popleft()

            # 2️⃣ Maintain decreasing order in deque
            while dq and nums[dq[-1]] < nums[i]:
                dq.pop()

            # 3️⃣ Add current index
            dq.append(i)

            # 4️⃣ Window formed → record max
            if i >= k - 1:
                res.append(nums[dq[0]])

        return res