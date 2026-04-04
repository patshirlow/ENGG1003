def sum_positives(nums):
    total = 0
    for n in nums:
        if n > 0:
            total += n
    return total

print(sum_positives([3, 4, 5])) # expect 12
print(sum_positives([-2, 3, -1, 4])) # expect 7
print(sum_positives([])) # expect 0