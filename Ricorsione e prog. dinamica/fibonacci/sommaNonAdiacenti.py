#data una lista di interi in input,
# ad esempio [3 2 7 10] dobbiamo trovare la somma
# massima di elementi non adiacenti
# utilizzando la prog. dinamica.

#[3 2 5 10 7] -> 15

def max_non_adiacent(nums: list):
    if not nums:
        return 0
    n = len(nums)
    if n==1:
        return max(0, nums[0])
    
    dp = [0]*n
    dp[0] = max(0, nums[0])
    dp[1] = max(dp[0], nums[1])

    for i in range(2, n):
        dp[i] = max(dp[i-1], dp[i-2]+nums[i])

    return dp[n-1]

nums = list(map(int, input().split()))
print(max_non_adiacent(nums))