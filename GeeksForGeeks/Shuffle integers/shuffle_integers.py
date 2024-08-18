class Solution:

    # https://discuss.geeksforgeeks.org/comment/c47ddf8b-b556-4f12-9a4d-ae15e39ca770/practice

    def shuffleArray(self, arr, n):
        # Set a large constant value for manipulating the array elements
        mx = int(1e4)  # 10**4

        # Initialize start and end indices
        start = 1
        end = n // 2

        # First loop to mix the elements in the array
        for i in range(1, n):
            if (i & 1) == 1:  # Check if the index is odd
                # For odd indices, place the element from the 'end' of the first half
                arr[i] = (arr[end] % mx) * mx + (arr[i] % mx)
                end += 1  # Move 'end' to the next element
            else:  # For even indices
                # Place the element from the 'start' of the first half
                arr[i] = (arr[start] % mx) * mx + (arr[i] % mx)
                start += 1  # Move 'start' to the next element

        # Second loop to extract the final shuffled elements
        for i in range(1, n):
            arr[i] //= mx  # Remove the old value by dividing by 'mx'


if __name__ == '__main__':
    n = 6
    a = [1, 2, 3, 4, 5, 6]
    ob = Solution()
    ob.shuffleArray(a, n)
    print(*a)
