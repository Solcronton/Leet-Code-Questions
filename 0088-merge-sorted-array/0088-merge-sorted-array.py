class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        k = []
        i = 0
        j = 0

        while i < m and j < n:
            if nums1[i] > nums2[j]:
                k.append(nums2[j])
                j += 1
            elif nums1[i] < nums2[j]:
                k.append(nums1[i])
                i += 1
            else:
                k.append(nums1[i])
                k.append(nums2[j])
                i += 1
                j += 1

        while i < m:
            k.append(nums1[i])
            i += 1

        while j < n:
            k.append(nums2[j])
            j += 1

        nums1[:] = k