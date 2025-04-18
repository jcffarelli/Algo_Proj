def partition(nums: list[int]) -> bool:
    if sum(nums) % 2 == 1: return False
    w: int = sum(nums) // 2
    n: int = len(nums)

    dp = [[False for i in range(n+1)] for j in range(w+1)]
    dp[0] = [True]*(n+1)

    for i in range(1,w+1):
        for j in range(1,n+1):
            dp[i][j] = dp[i][j-1] or i-nums[j-1] >= 0 and dp[i-nums[j-1]][j-1]

    return dp[w][n]

def main():
    nums = list(map(int, input().split()))
    print(partition(nums))

if __name__ == "__main__":
    main()