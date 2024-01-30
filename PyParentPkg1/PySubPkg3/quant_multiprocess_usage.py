import random
from concurrent.futures import ProcessPoolExecutor

result = list()


def append_result(r):
    result.append(r.result())


def generate_random():
    return random.randint(0, 100)


if __name__ == '__main__':
    with ProcessPoolExecutor() as pool:
        for i in range(100):
            future_result = pool.submit(generate_random)
            future_result.add_done_callback(append_result)

    for v in result:
        print(v)