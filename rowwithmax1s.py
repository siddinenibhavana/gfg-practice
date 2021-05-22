#User function Template for python3
#row with max 1s
class Solution:

	def rowWithMax1s(self,arr, n, m):
	    L=[]
		for i in range(0,n):
		    e=arr[i].count(1)
		    L.append(e)
		m=max(L)
		if m==0:
		    return -1
		else:
		    return L.index(m)

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n, m = list(map(int, input().strip().split()))
        
        inputLine = list(map(int, input().strip().split()))
        arr = [[0 for j in range(m)] for i in range(n)]
        
        for i in range(n):
            for j in range(m):
                arr[i][j] = inputLine[i * m + j]
        ob = Solution()
        ans = ob.rowWithMax1s(arr, n, m)
        print(ans)
        tc -= 1

# } Driver Code Ends
