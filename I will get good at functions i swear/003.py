# 7)
def sum_first_n(n):
    total = 0
    for i in range(n + 1):
        total += i
    return total
print(sum_first_n(10))

# 8)
def count_negatives(lst):
    count = 0 # used for counting negatives
    i = 0 # current index

    while i < len(lst):
        if lst[i] < 0:
            count += 1
        i += 1 # moves to the next element
    return count
print(count_negatives([-1, 4, -6]))

# task 7
def reverse_string(s):
    rev = ""
    for ch in s:
        rev = ch + rev
    return rev
print(reverse_string("yag"))