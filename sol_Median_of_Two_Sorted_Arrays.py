"""
Example 1:

nums1 = [1, 3]
nums2 = [2]

The median is 2.0
Example 2:

nums1 = [1, 2]
nums2 = [3, 4]

The median is (2 + 3)/2 = 2.5
"""


class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums3 = []
        i = j = 0
        len1 = len(nums1)
        len2 = len(nums2)

        while i < len1 and j < len2:
            if nums1[i] <= nums2[j]:
                nums3.append(nums1[i])
                i += 1
            else:
                nums3.append(nums2[j])
                j += 1

        while i < len1:
            nums3.append(nums1[i])
            i += 1

        while j < len2:
            nums3.append(nums2[j])
            j += 1

        if (len1 + len2) % 2 != 0:
            return nums3[(len1 + len2) // 2]
        else:
            return (nums3[(len1 + len2) // 2 - 1] + nums3[(len1 + len2) // 2]) / 2

        return nums3
