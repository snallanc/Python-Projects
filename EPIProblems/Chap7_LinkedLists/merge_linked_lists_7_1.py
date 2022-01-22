"""
EPI Problem 7.1: Merge two sorted lists L1 and L2.
Eg: L1: 2 -> 5 -> 7, L2: 3 -> 11
    R:  2 -> 3 -> 5 -> 7 -> 11
"""

"""
Solution 1: Naive approach with O(n) time and O(n) space complexity
Walk through each list, find the smallest node, create a node and copy the smallest node into the result list. 
"""

"""
Solution 2: Just re-arrange the elements of the given lists without using extra space.
Time Compl: O(n)
Space Compl: O(1) 
"""

from datastructures.LinkedList import *
def merge_sorted_lists(L1, L2):
    e1, e2, res_prev_e, result = L1.head, L2.head, None, None
    while e1 and e2:
        min_e = e1 if e1.data < e2.data else e2
        if not res_prev_e:
            res_prev_e = min_e
            result = res_prev_e
        else:
            res_prev_e.next = min_e
            res_prev_e = min_e
        if e1 == min_e:
            e1 = e1.next
        else:
            e2 = e2.next
    res_prev_e.next = e1 if e1 else e2
    return result

"""
Test code
"""

if __name__ == "__main__":
    L1 = LinkedList()
    L2 = LinkedList()
    for e in [1,3,5,7,9]:
        L1.insert_node(e)
    for e in [2,4,6,8,10]:
        L2.insert_node(e)
    print("Lists before merge:")
    L1.print_list()
    L2.print_list()
    merge_sorted_lists(L1, L2)
    print("List after merge:")
    L1.print_list()