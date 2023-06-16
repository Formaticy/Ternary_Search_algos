#ТЕРНАРНЫЙ ПОИСК ЭЛЕМЕНТА В ОТСОРТИРОВАННОМ МАССИВЕ ПО ВОЗРАСТАНИЮ И УБЫВАНИЮ СООТВЕТСТВЕННО
def ternary_search_increase(sequence, element):
    l = 0
    r = len(sequence) - 1
    while l <= r:
        m1 = l + (r - l) // 3
        m2 = r - (r - l) // 3
        if sequence[m1] == element:
            return m1
        if sequence[m2] == element:
            return m2
        if sequence[m1] < element < sequence[m2]:
            l = m1 + 1
            r = m2 - 1
        elif element < sequence[m1]:
            r = m1 - 1
        else:
            l = m2 + 1
    return None


def ternary_search_decrease(sequence, element):
    l = 0
    r = len(sequence) - 1
    while l <= r:
        m1 = l + (r - l) // 3
        m2 = r - (r - l) // 3
        if sequence[m1] == element:
            return m1
        if sequence[m2] == element:
            return m2
        if sequence[m1] > element > sequence[m2]:
            l = m1 + 1
            r = m2 - 1
        elif element > sequence[m1]:
            r = m1 - 1
        else:
            l = m2 + 1
    return None
