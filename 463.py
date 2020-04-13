'''
463.  Island Perimete

You are given a map in form of a two-dimensional integer grid where 1 represents land and 0 represents water.

Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells).

The island doesn't have "lakes" (water inside that isn't connected to the water around the island). One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.

 

Example:

Input:
[[0,1,0,0],
 [1,1,1,0],
 [0,1,0,0],
 [1,1,0,0]]

Output: 16

Explanation: The perimeter is the 16 yellow stripes in the image below:



'''

class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        i=j=0
        edge=0
        while i < len(grid):
            
            while j < len(grid[i]):
                
                if grid[i][j] == 1:
                    #Left
                    if((j-1 >= 0 and grid[i][j-1] == 0) or j-1<0):
                        edge+=1

                    #Right
                    if (j+1 >= len(grid[i]) or (j+1 < len(grid[i]) and grid[i][j+1] == 0)) :
                        edge+=1

                    #Top
                    if (i-1 < 0 or grid[i-1][j] == 0):
                        edge+=1

                    #Bottom
                    if (i+1 >= len(grid) or grid[i+1][j] == 0):
                        edge+=1 
                j+=1
               
            i+=1
            j=0
        
        return edge
                