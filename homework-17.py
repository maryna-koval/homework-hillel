def change(lst):
    if len(lst) >= 2:
        lst[0], lst[-1] = lst[-1], lst[0]
    else:
        print("У списку повинно бути щонайменше 2 елементи.")
    return lst


new_list = [2, 4, 5, 6]
print(change(new_list))


def to_dict(lst):
    return {x: x for x in lst}


new_list = ['a', 'b', 'c', 'd']
print(to_dict(new_list))


def sum_range(start, end):
    if start > end:
        start, end = end, start
    result = sum(range(start, end + 1))
    return result


start = int(input("Введіть значення start: "))
end = int(input("Введіть значення end: "))
print(f'Сума чисел:{sum_range(start, end)}')
