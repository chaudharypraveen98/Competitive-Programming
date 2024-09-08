from collections import Counter

no_of_shoes = int(input())
shoe_sizes = list(map(int, input().split()))
no_of_customers = int(input())
stocks = Counter(shoe_sizes)


def get_profit(stocks, no_of_customers):
    profit = 0
    for i in range(no_of_customers):
        required_size, price = map(int, input().split())
        if stocks[required_size]:
            profit += price
            stocks[required_size] -= 1
    return profit


print(get_profit(stocks, no_of_customers))
