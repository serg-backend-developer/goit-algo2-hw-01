def find_min_and_max(values):
    if not values:
        return None, None

    def search_min_max(left, right):
        if left == right:
            return values[left], values[left]
        if right == left + 1:
            return min(values[left], values[right]), max(values[left], values[right])

        mid = (left + right) // 2
        left_min, left_max = search_min_max(left, mid)
        right_min, right_max = search_min_max(mid + 1, right)
        return min(left_min, right_min), max(left_max, right_max)

    return search_min_max(0, len(values) - 1)


print(find_min_and_max([12, 34, 56, 78, 90]))
# (12, 90)
print(find_min_and_max([-5, -1, -8, -3, -10]))
# (-10, -1)
print(find_min_and_max([42]))
# (42, 42)
print(find_min_and_max([]))
# (None, None)
print(find_min_and_max([7, 7, 7, 7, 7]))
# (7, 7)