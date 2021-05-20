#largest number formed by an array
from itertools import permutations
class Solution:

    def printLargest(self,arr):
        L=[]
        perm = permutations(arr)
        for i in list(perm):
            a="".join(i)
            L.append(int(a))
        return max(L)
#{ 
#  Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(str, input().strip().split()))
        ob = Solution()
        ans = ob.printLargest(arr)
        print(ans)
        tc -= 1
# } Driver Code Ends
