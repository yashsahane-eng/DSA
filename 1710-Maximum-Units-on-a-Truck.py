class Solution(object):
    def maximumUnits(self, boxTypes, truckSize):
        """
        :type boxTypes: List[List[int]]
        :type truckSize: int
        :rtype: int
        """

        boxTypes.sort(key=lambda x:x[1], reverse=True)

        total=0

        for numberOfBoxes , unitsPerBox in boxTypes:
            boxes=min(numberOfBoxes ,truckSize)


            total += boxes*unitsPerBox

            truckSize -=boxes

            if truckSize ==0:
                break

        return total
        