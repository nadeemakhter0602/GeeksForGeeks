class Solution:

	def findMaximum(self,arr, n):
		# code here
        if arr[-1] > arr[-2]:
            return arr[-1]
        l = 0
        r = n - 1
        max_ = float('-inf')
        while l <= r:
            mid = (l + r) // 2
            max_ = max(arr[mid], max_)
            if mid + 1 < n:
                if arr[mid + 1] < arr[mid]:
                    r = mid - 1
                elif arr[mid + 1] > arr[mid]:
                    l = mid + 1
        return max_