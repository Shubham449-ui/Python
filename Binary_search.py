def binary_search(sorted_nums, target):
    left = 0
    right = len(sorted_nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if sorted_nums[mid] == target:
            return mid
        elif sorted_nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


arr = [14, 20, 36, 11, 4, 5, 21]
target_element = 11
arr.sort()
print("Sorted Array :: ",arr)
result = binary_search(arr, target_element)

if result != -1:
    print(f"Element {target_element} is found at index {result}")
else:
    print(f"Element {target_element} is not found")
