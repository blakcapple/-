import random
def find(nums, k):
    def partition(nums, left_idx, right_idx):
        pivot=  nums[left_idx]
        begin = left_idx
        while left_idx < right_idx:
            while left_idx < right_idx and nums[right_idx] <= pivot:
                right_idx -= 1
            while left_idx < right_idx and nums[left_idx] >= pivot:
                left_idx += 1
            if left_idx < right_idx:
                nums[left_idx], nums[right_idx] = nums[right_idx], nums[left_idx]
        nums[begin], nums[left_idx] = nums[left_idx], nums[begin]
        return left_idx
    n = len(nums)
    left_idx = 0
    right_idx = n-1
    while True:
        idx = partition(nums, left_idx, right_idx)
        if idx == (k-1):
            return nums[idx]
        elif idx < k-1:
            left_idx = idx + 1
        else:
            right_idx = idx - 1
nums = [random.randint(1,100) for i in range(10)]
print(nums)
print(find(nums, 3))
        