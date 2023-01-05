class Solution:
    def solve(self, N : int) -> int:
        # code here
        time = 0
        while N > 0:
            if N % 2 == 0:
                N -= int(N / 2)
            else:
                N -= int((N + 1) / 2)
            time += 1
        return time