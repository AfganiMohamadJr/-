import concurrent.futures
import threading
import time


class BancAccount:
    def __init__(self):
        self.balance = 100
        self.lock = threading.Lock()

    def update(self, transaction, amount):
        print(f'{transaction} started')

        with self.lock:
            tmp_amount = self.balance
            tmp_amount += amount
            time.sleep(1)
            self.balance = tmp_amount
        print(f'{transaction} ended')


if __name__ == '__main__':
    # lock = threading.Lock()
    # print(lock.locked())
    # # False
    #
    # lock.acquire()
    # print(lock.locked())
    # # True
    #
    # tmp_amount = self.balance
    # tmp_amount += amount
    # time.sleep(1)
    # self.balance = tmp_amount
    #
    # lock.release()
    # print(lock.locked())
    # # False

    acc = BancAccount()
    print(acc.balance)

    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as ex:
        ex.map(acc.update, ('refill', 'withdraw'), (100, -200))

    print(f"balasce={acc.balance}")
