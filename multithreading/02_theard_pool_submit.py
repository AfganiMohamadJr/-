import concurrent.futures
import time


def div(divisor: int, limit: int) -> int:
    print(f'started div={divisor}')

    count = 0
    for i in range(1, limit):
        if i % divisor == 0:
            count += i
        # print(f'divisor={divisor}, i={i}')
        time.sleep(0.2)
    print(f'ended={divisor}', end='\n')
    return count


if __name__ == '__main__':
    print('started main')

    future = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        future.append(executor.submit(div, 3, 20))
        future.append(executor.submit(div, 5, 25))

        while not (future[0].done() and future[1].done()):
            print('/', end='')
            time.sleep(0.5)

        for f in future:
            print(f.result())


