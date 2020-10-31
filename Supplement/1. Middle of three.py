'''
Test inputs:
        t = testcase
        Input:
        A = 978, B = 518, C = 300
        Output:
        518

'''

class Solution:
    def middle(self,A,B,C):
        #code here
        if A>B and B>C or C>B and B>A:
            return B
        elif B>A and A>C or C>A and A>B:
            return A
        else:
            return C




#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        A,B,C=map(int,input().strip().split())
        ob=Solution()
        print(ob.middle(A,B,C))
# } Driver Code Ends
