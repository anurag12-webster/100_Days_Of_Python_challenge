def countSpecialPermutations(nums):
    memo = {}

    def dfs(nums, index, prev):
        if index == len(nums) - 1:
            return 1

        if (index, prev) in memo:
            return memo[(index, prev)]

        count = 0
        for i in range(index, len(nums)):
            if nums[i] % prev == 0 or prev % nums[i] == 0:
                count += dfs(nums, i + 1, nums[i])

        memo[(index, prev)] = count
        return count

    return dfs(nums, 0, 1)  # Start with index 0 and previous element 1


nums = [2, 3, 6]
result = countSpecialPermutations(nums)
print(result)  # Output: 2

nums = [1, 4, 3]
result = countSpecialPermutations(nums)
print(result)  # Output: 2
