class Solution:
    def MissingNumber(self,array,n):
        # code here
        array_set = set(array)
        for i in range(1, n + 1):
            if i not in array_set:
                return i