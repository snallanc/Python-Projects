"""
Problem: Given a list of stock prices, find the maximum profit that can be made by buying and selling the stock multiple times. You must sell the stock before you buy again.
Pattern: Heap-based profit calculation
Key insight: Use a min-heap to keep track of the lowest prices and calculate profit when a higher price is encountered.
Time Complexity: O(n log n) - every price is pushed and popped from the heap at most once each involving logn steps
Space Complexity: O(n)
"""
import heapq

def max_stack_profit(prices = []):
    min_heap = []
    max_profit = 0
    if not prices or len(prices) < 2:
        return 0

    for price in prices:
        if min_heap and price > min_heap[0]:
            max_profit += price - min_heap[0]
            heapq.heappop(min_heap)
        heapq.heappush(min_heap, price)
    return max_profit

"""
Optimized version of the max_stack_profit function that calculates the maximum profit in O(n) time and O(1) space.
"""
def max_stack_profit_optimized(prices=[]):
    max_profit = 0
    if not prices or len(prices) < 2:
        return 0
    for idx in range(1, len(prices)):
        if prices[idx] > prices[idx - 1]:
            max_profit += prices[idx] - prices[idx - 1]
    return max_profit

"""Test Code"""
if __name__ == "__main__":
    test_cases = [[7,1,5,3,6,4], [1,2,3,4,5], [7,6,4,3,1], [], [1], [1, 2], [2, 1]]
    for prices in test_cases:
        print(f"Heap Based => Input: {prices}, Output: {max_stack_profit(prices)}")
        print(f"Optimized => Input: {prices}, Output: {max_stack_profit_optimized(prices)}")