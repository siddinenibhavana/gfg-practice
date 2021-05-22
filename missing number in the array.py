#missing number in the array
class Solution:
    def MissingNumber(self,array,n):
        l=len(array)
        tot=(l+1)*(l+2)/2
        s=sum(array)
        return int(tot-s)
#{ 
#  Driver Code Starts
#Initial Template for Python 3




t=int(input())
for _ in range(0,t):
    n=int(input())
    a=list(map(int,input().split()))
    s=Solution().MissingNumber(a,n)
    print(s)
# } Driver Code Ends
