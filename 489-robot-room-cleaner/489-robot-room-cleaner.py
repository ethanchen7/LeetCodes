# """
# This is the robot's control interface.
# You should not implement it, or speculate about its implementation
# """
#class Robot:
#    def move(self):
#        """
#        Returns true if the cell in front is open and robot moves into the cell.
#        Returns false if the cell in front is blocked and robot stays in the current cell.
#        :rtype bool
#        """
#
#    def turnLeft(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def turnRight(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def clean(self):
#        """
#        Clean the current cell.
#        :rtype void
#        """

class Solution:
    def cleanRoom(self, robot):
        """
        :type robot: Robot
        :rtype: None
        """
        
        def goBack():
            robot.turnRight()
            robot.turnRight()
            robot.move()
            robot.turnRight()
            robot.turnRight()
        
        def getNewDirection(currDirection):
            # 0 -> up, 1 -> right, 2 -> down, 3 -> left
            directions = [(-1,0,0),(0,1,1),(1,0,2),(0,-1,3)]
            return directions[currDirection:] + directions[:currDirection]
        
        def canMove(x,y):
            return (x,y) not in visited and robot.move()
        
        def helper(x,y,d):
            robot.clean()
            visited.add((x,y))
            
            newDirections = getNewDirection(d)
            for i in range(4): # check all four directions
                direction = newDirections[i]
                nx, ny, nd = x + direction[0], y + direction[1], direction[2]
                if canMove(nx, ny):
                    helper(nx, ny, nd)
                
                robot.turnRight() # turn right to go to the next direction in the loop
            goBack() # backtrack and maintain orientation
           
        visited = set()
        helper(0,0,0)