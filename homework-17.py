def change(lst):
    if len(lst) >= 2:
        lst[0], lst[-1] = lst[-1], lst[0]
    else:
        print("У списку повинно бути щонайменше 2 елементи.")
    print(lst)


new_list = [2, 4, 5, 6]
change(new_list)


def to_dict(lst):
     dictionary = dict((x, x) for x in lst)
     print(dictionary)


new_list = ['a', 'b', 'c', 'd']
to_dict(new_list)


def sum_range(start, end):
     if start > end:
          start, end = end, start
     result = sum(range(start, end + 1))
     print("Сума чисел:", result)


start = int(input("Введіть значення start: "))
end = int(input("Введіть значення end: "))
sum_range(start, end)
