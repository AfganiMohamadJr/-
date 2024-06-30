import concurrent.futures
from multithreading.there_count_sum import read_file, there_count_sum


if __name__ == '__main__':

    data_file1K = read_file("..\\data\\1Kints.txt")

    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        flow = executor.map(there_count_sum, (data_file1K, data_file1K), ('t1', 't2'))
        for i in flow:
            print(f'{i=}')







