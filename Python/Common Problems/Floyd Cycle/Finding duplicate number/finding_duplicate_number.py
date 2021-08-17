# function to find one duplicate
def findduplicate(arr):
    if len(arr) <= 1:
        return -1

    # initialize fast and slow
    slow = arr[0]
    fast = arr[arr[0]]

    # loop to enter in the cycle
    while fast != slow:
        # move one step for slow
        slow = arr[slow]

        # move two step for fast
        fast = arr[arr[fast]]

    # loop to find entry point of the cycle
    fast = 0
    while slow != fast:
        slow = arr[slow]
        fast = arr[fast]
    return slow


# Driver Code
if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6, 3]
    n = len(arr)
    print(findduplicate(arr))
