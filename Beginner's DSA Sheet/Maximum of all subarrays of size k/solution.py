from collections import deque

class Solution:
    
    #Function to find maximum of each subarray of size k.
    def max_of_subarrays(self,arr,n,k):
        #code here
        window = deque()
        decreasing = deque()
        s = []
        for i in range(n):
            while len(decreasing) > 0 and decreasing[-1] < arr[i]:
                decreasing.pop()
            decreasing.append(arr[i])
            window.append(arr[i])
            if len(window) == k:
                if decreasing[0] == window[0]:
                    max_ = decreasing.popleft()
                    s.append(max_)
                else:
                    s.append(decreasing[0])
                window.popleft()
        return s