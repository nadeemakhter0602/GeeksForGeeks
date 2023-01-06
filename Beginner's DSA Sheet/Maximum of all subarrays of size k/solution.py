from collections import deque

class Solution:
    
    #Function to find maximum of each subarray of size k.
    def max_of_subarrays(self,arr,n,k):
        #code here
        decreasing = deque()
        s = []
        for i in range(n):
            while len(decreasing) > 0 and decreasing[-1] < arr[i]:
                decreasing.pop()
            decreasing.append(arr[i])
            if i - k + 1 >= 0:
                if decreasing[0] == arr[i - k + 1]:
                    max_ = decreasing.popleft()
                    s.append(max_)
                else:
                    s.append(decreasing[0])
        return s