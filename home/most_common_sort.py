from collections import Counter

def frequency_sort(items):
    frequency_map = Counter(items)    
    for item, frequency in frequency_map.most_common():
        yield from [item]*frequency


print("Example:")
print(frequency_sort([4, 6, 2, 2, 6, 4, 4, 4]))

assert list(frequency_sort([4, 6, 2, 2, 6, 4, 4, 4])) == [4, 4, 4, 4, 6, 6, 2, 2]
assert list(frequency_sort(['bob', 'bob', 'carl', 'alex', 'bob'])) == ['bob', 'bob', 'bob', 'carl', 'alex']
assert list(frequency_sort([17, 99, 42])) == [17, 99, 42]
assert list(frequency_sort([])) == []
assert list(frequency_sort([1])) == [1]
print("Coding complete? Click 'Check' to earn cool rewards!")

