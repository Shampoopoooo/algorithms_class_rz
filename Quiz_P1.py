def sortColors(nums: list[int]) -> None:
    # Step 1: Count each color
    count = [0, 0, 0]
    for num in nums:
        count[num] += 1
    
    # Step 2: Overwrite array in-place
    idx = 0
    for color in range(3):
        for _ in range(count[color]):
            nums[idx] = color
            idx += 1
