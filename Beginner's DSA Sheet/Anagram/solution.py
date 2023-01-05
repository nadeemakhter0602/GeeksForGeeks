class Solution:
    
    #Function is to check whether two strings are anagram of each other or not.
    def isAnagram(self,a,b):
        #code here
        if len(a) != len(b):
            return False
        map_a = [0] * 26
        map_b = [0] * 26
        for i in range(len(a)):
            map_a[ord(a[i]) - ord('a')] += 1
            map_b[ord(b[i]) - ord('a')] += 1
        return map_a == map_b