class Solution(object):

    def power(self,x,n):

        if n==0:
            return 1.0

        if n==1:
            return x

        if n%2==0:
            return self.power(x*x ,n//2)

        return x*self.power(x,n-1)


    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        num=n

        if n<0:
            return 1.0 / self.power(x,-num)

        return self.power(x,num)
        