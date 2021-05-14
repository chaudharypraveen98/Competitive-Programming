# Recursive solution with memo table
def knapsack(index, W):
    # if the value is already calculated
    if array[index][W] != -1:
        return array[index][W]

    # When index ie zero or total available space is over
    if index == 0 or W == 0:
        result = 0

    # If the value at that index is greater than total available space
    elif weight[index] > W:
        result = knapsack(index - 1, W)

    # we will calculate the max value by including or excluding this element.
    else:
        temp1 = knapsack(index - 1, W)
        temp2 = values[index] + knapsack(index - 1, W - weight[index])
        result = max(temp1, temp2)
    array[index][W] = result
    return result


if __name__ == '__main__':
    weight = [10, 20, 30, 40, 50]
    values = [60, 100, 120, 135, 200]
    max_weight = 100
    length = len(weight)

    # intialising the array
    array = [[-1 for col in range(max_weight + 1)] for row in range(length + 1)]
    final_result = knapsack(length - 1, max_weight)
    print(final_result)
