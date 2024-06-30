import threading
from multithreading.there_count_sum import read_file, there_count_sum

if __name__ == '__main__':
    print("started main")

    lst_from_file = read_file("..\\data\\1Kints.txt")

    test_thread = threading.Thread(target=there_count_sum, args=(lst_from_file,), daemon=True)
    test_thread.start()  # начинает поток test_thread
    test_thread.join()  # ждём завершения потока test_thread

    print("Ждешь да?")
