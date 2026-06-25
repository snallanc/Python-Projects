"""
Problem: Container With Most Water
Given n non-negative integers a1, a2, ..., an , where each represents height of a line
at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai)
and (i, 0). Find two lines, which together with x-axis forms a container, such that the container
contains the most water ie., max area.
Pattern: Two Pointers on either side of the array
Time Complexity: O(n)
Space Complexity: O(1)
"""

def max_area(heights: list[int]) -> int:
    if not heights or len(heights) == 0:
        return 0
    l, r, max_area = 0, len(heights)-1, 0
    while l < r:
        min_h = min(heights[l], heights[r])
        area = min_h * abs(r-l)
        if area > max_area:
            max_area = area
        if min_h == heights[r]:
            r -= 1
        else:
            l +=1
    return max_area 

"""Test code"""
if __name__ == "__main__":
    heights = [[1,8,6,2,5,4,8,3,7], 
               [1,1], 
               [4,3,2,1,4], 
               [1,2,1], 
               [1,2,4,3]] 
    for h in heights:
        print(f"Max area for {h}: {max_area(h)}")