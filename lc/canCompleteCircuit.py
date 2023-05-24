class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas)<sum(cost):
            return -1

        total = 0
        res = 0

        for i in range(len(gas)):
            total += gas[i] - cost[i]

            if total < 0:
                total=0
                res=i+1
        return res


# Time limit exceeded
# class Solution:
#     def canCompleteCircuit(self, gas, cost):
#         totalStations = len(gas)

#         initialGasFilled = 0

#         for i in range(totalStations):
#             if((gas[i]>=cost[i]) and (gas[i]>0)):
#                 initialGasFilled = gas[i]
#                 keepDriving=True
#                 gasStation = i
#                 gasAvailable = initialGasFilled
#                 while keepDriving:
#                     if gasAvailable >= cost[gasStation]:
#                         gasAvailable = (gasAvailable-cost[gasStation])+gas[(gasStation+1)%totalStations]
#                         gasStation=(gasStation+1)%totalStations

#                         if gasStation==i:
#                             return gasStation
#                     else:
#                         keepDriving=False

#         return -1

sln = Solution()

result = sln.canCompleteCircuit([2,3,4],[3,4,3])
print("Result: ",result)