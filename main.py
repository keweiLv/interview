from typing import List


def threeSum(nums: List[int]) -> List[List[int]]:
    nums.sort()
    n = len(nums)
    result = []

    for i in range(n-2):
        if i > 0 and nums[i] == nums[i-1]:
            continue

        target = -nums[i]
        left, right = i+1, n-1
        while left < right:
            current_sum = nums[left] + nums[right]
            if current_sum == target:
                result.append([nums[i], nums[left], nums[right]])
                while left < right and nums[left] == nums[left+1]:
                    left += 1
                while left < right and nums[right] == nums[right-1]:
                    right -= 1
                left += 1
                right -= 1
            elif current_sum < target:
                left += 1
            else:
                right -= 1
    return result


def main():
    nums = [-100,-70,-60,110,120,130,160]
    res = threeSum(nums)
    print(res)


if __name__ == "__main__":
    main()
