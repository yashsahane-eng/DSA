class Solution(object):
    def totalFruit(self, fruits):
        """
        :type fruits: List[int]
        :rtype: int
        """
        maxLen=0

        n=len(fruits)

        for i in range (n):
            s=set()

            for j in range(i,n):
                s.add(fruits[j])

                if len(s)<=2:
                    Len=j-i+1

                    maxLen=max(maxLen , Len)

                else:
                    break
        return maxLen
        