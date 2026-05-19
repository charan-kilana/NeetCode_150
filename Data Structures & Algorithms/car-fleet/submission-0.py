class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        # Brute Force Method

        # Calculate the time taken to reach the target
        timeTaken = []
        fleetNumber = 0
        for i in range(len(position)):
            time = (target - position[i])/speed[i]
            timeTaken.append([position[i],time])
        
        # Sort it acc to the position\
        timeTaken.sort(reverse=True)
        slowestTime = 0
        for i in range(len(timeTaken)):
            if timeTaken[i][1] > slowestTime:
                slowestTime = timeTaken[i][1]
                fleetNumber = fleetNumber + 1
        return fleetNumber
            

        