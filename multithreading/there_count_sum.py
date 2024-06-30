def read_file(path):
    lst = []
    with open(path, 'r') as file:
        while line := file.readline():
            lst.append(int(line))
    return lst


def there_count_sum(lst, tread_name='t'):  # поиск 3 чисел дающих 0 в сумме
    print(f"Начало поиска {tread_name}")

    n = len(lst)
    count = 0

    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if lst[i] + lst[j] + lst[k] == 0:
                    print(f"Triple in {tread_name}: {lst[i]} {lst[j]} {lst[k]}")
                    count += 1
    print(f"The end {tread_name}")
    return count
