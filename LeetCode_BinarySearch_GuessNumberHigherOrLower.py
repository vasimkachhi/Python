from sys import stdin as Si 


class Solution(object):
    def guessNumber(self, n):
        s,e=1,n
        if self.guess(s)==0:    return s
        
        while s<=e:
            m = int((s+e)/2)
            r = self.guess(m)
            print(s,e,m,r)
            if r==0:   return m
            elif r==-1: e=m-1
            else:   s=m+1

    def guess(self,r):
        x=8
        if r==x:    return 0
        elif r<x:   return 1
        elif r>x:   return -1 
        
            

if __name__=='__main__':
    S= Solution()
    for i in range(int(Si.readline())): 
        print(S.guessNumber(int(Si.readline())))
    


'''
Guess Number Higher or Lower

We are playing the Guess Game. The game is as follows:

I pick a number from 1 to n. You have to guess which number I picked.

Every time you guess wrong, I'll tell you whether the number is higher or lower.

You call a pre-defined API guess(int num) which returns 3 possible results (-1, 1, or 0):

1 : My number is lower
 1 : My number is higher
 0 : Congrats! You got it!
Example:
n = 10, I pick 6.

Return 6.

'''

