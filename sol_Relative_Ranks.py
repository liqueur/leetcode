
class Solution:
    def findRelativeRanks(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        medals = {
            1: "Gold Medal",
            2: "Silver Medal",
            3: "Bronze Medal",
        }

        from queue import PriorityQueue

        q = PriorityQueue()

        for i, n in enumerate(nums):
            q.put((-n, i))

        cnt = 1
        while q.qsize():
            _, i = q.get()
            if cnt in medals:
                nums[i] = medals[cnt]
            else:
                nums[i] = str(cnt)

            cnt += 1

        return nums

