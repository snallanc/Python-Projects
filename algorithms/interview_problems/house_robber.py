def house_robber(house_money=[]):
    if not house_money:
        return 0
    if len(house_money) == 1:
        return house_money[0]
    p1, p2 = house_money[0], max(house_money[0], house_money[1])
    for i in range(2, len(house_money)):
        p1, p2 = p2, max(p2, p1 + house_money[i])
    return p2

# Test code
if __name__ == "__main__":
    test_cases = [
        [1, 2, 3, 1],
        [2, 7, 9, 3, 1],
        [2, 1, 1, 2],
        [0],
        [1],
        [1, 2],
        [2, 1],
    ]
    for i, test in enumerate(test_cases):
        print("Test case {}: House money = {}, Max loot = {}".format(i+1, test, house_robber(test)))