# Bottom up with dynamic programming
def knapsack(index, W):
    array = [[0 for col in range(max_weight + 1)] for row in range(length + 1)]
    max_value = 0

    # Iterating over items and values
    for i in range(index - 1, -1, -1):
        for j in range(W - 1, -1, -1):

            # If weight of item is greater than the
            if weight[i] > W:
                array[i][j] = 0
            else:
                W -= weight[i]
                # Should we drop this item. Let's take both of both and take max of both
                array[i][j] = values[i] + max(array[i + 1][j], array[i][j + 1])
                max_value += array[i][j]
    return max_value


if __name__ == '__main__':
    weight = [10, 20, 30]
    values = [60, 100, 120]
    max_weight = 50
    length = len(weight)
    print(knapsack(length, max_weight))
