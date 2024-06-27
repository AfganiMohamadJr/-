import threading


def read_file(path):
    lst = []
    with open(path, 'r') as file:
        while line := file.readline():
            lst.append(int(line))
    return lst


def there_count_sum(lst):
    print("Начало поиска")

    n = len(lst)
    count = 0

    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if lst[i] + lst[j] + lst[k] == 0:
                    print(f"Triple {lst[i]} {lst[j]} {lst[k]}")
                    count += 1

    print("The end")


if __name__ == '__main__':
    print("started main")

    lst_from_file = read_file("..\\data\\1Kints.txt")

    test_thread = threading.Thread(target=there_count_sum, args=(lst_from_file,), daemon=True)
    test_thread.start()
    test_thread.join()

    print("Ждешь да?")
