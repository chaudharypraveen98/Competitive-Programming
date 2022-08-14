def is_hoppable(tower, memo, index):
    # If we are able to get out
    if index >= len(tower):
        return True

    # If the height of tower is zero, so we can't move forward
    if tower[index] == 0:
        return False

    possible_paths = set()
    for i in range(index+tower[index], index, -1):
        # Checking in memo table and not alvailable
        if i not in memo:
            possible = is_hoppable(tower, memo, i)
            memo[i] = possible
            possible_paths.add(possible)

    # It will check if any tower leads to lead or not
    memo[index] = any(possible_paths)
    return memo[index]


# array = list(map(int,input().split()))
array = [4, 2, 0, 0, 2]
print(is_hoppable(array, {}, 0))
