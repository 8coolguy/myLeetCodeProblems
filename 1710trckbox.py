class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda box: box[1], reverse=True)
        totalUnits = 0
        for i,j in boxTypes:
            tmp =min(truckSize,i)
            totalUnits+=tmp*j
            truckSize -= tmp
        return totalUnits
            
            
