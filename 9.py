import timeit

# Greedy algorithm to find the optimal way to give change
def find_coins_greedy(amount, coins):
    coins_count = {}
    for coin in coins:
        count = amount // coin  # How many of this coin can be used
        if count:
            coins_count[coin] = count
        amount -= coin * count  # Subtract the value of used coins
        if amount == 0:
            break
    return coins_count

# Dynamic programming to find the minimal number of coins needed for a given amount
def find_min_coins(amount, coins):
    min_coins_required = [0] + [float('inf')] * amount
    coin_used = [0] * (amount + 1)

    for sub_sum in range(1, amount + 1):
        for coin in coins:
            if sub_sum >= coin and min_coins_required[sub_sum - coin] + 1 < min_coins_required[sub_sum]:
                min_coins_required[sub_sum] = min_coins_required[sub_sum - coin] + 1
                coin_used[sub_sum] = coin

    # Reconstruct the used coins
    coins_count = {}
    current_sum = amount
    while current_sum > 0:
        coin = coin_used[current_sum]
        coins_count[coin] = coins_count.get(coin, 0) + 1
        current_sum -= coin

    return coins_count

if __name__ == '__main__':
    # Coin denominations
    coins = [50, 25, 10, 5, 2, 1]

    # Test cases with different amounts
    cases = [137, 543210, 113, 89]

    functions = [find_coins_greedy, find_min_coins]

    # Compare performance and results
    for amount in cases:
        print(f"\nCase for sum: {amount}")
        for fun in functions:
            start_time = timeit.default_timer()
            result = fun(amount, coins)
            time_taken = timeit.default_timer() - start_time
            print(f"Result for {fun.__name__}: {result}")
            print(f"Time taken for {fun.__name__}: {time_taken:.6f} seconds")