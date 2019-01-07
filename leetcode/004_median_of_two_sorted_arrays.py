##SOLUTION 1: 164 ms

class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        # import heapq
            # nums = list(heapq.merge(nums1, nums2))
        nums = nums1 + nums2
        nums.sort()
        l = len(nums)
        if l & 1:
            return nums[l // 2]
        else:
            return sum(nums[l//2 - 1 : (l//2) + 1]) / 2
            # return (nums[l//2 - 1] + nums[l//2]) / 2    no difference

##SOLUTION 2: 140 ms
class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        l1 = len(nums1)
        l2 = len(nums2)
        if l1 == 0:
            if l2 & 1:
                return nums2[l2 // 2]
            else:
                return (nums2[l2//2 - 1] + nums2[l2//2]) / 2
        elif l2 == 0:
            if l1 & 1:
                return nums1[l1 // 2]
            else:
                return (nums1[l1//2 - 1] + nums1[l1//2]) / 2
        else:
            nums = nums1 + nums2
            nums.sort()
            l = l1 + l2
            if l & 1:
                return nums[l // 2]
            else:
                return ((nums[l//2 - 1] + nums[l//2]) / 2)
