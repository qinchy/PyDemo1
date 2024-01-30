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

    array1 = [[[[1., 1., 1.], [1., 1., 1.], [1., 1., 1.]], [[1., 1., 1.], [1., 1., 1.], [1., 1., 1.]],
               [[1., 1., 1.], [1., 1., 1.], [1., 1., 1.]]],
              [[[1., 1., 1.], [1., 1., 1.], [1., 1., 1.]], [[1., 1., 1.], [1., 1., 1.], [1., 1., 1.]],
               [[1., 1., 1.], [1., 1., 1.], [1., 1., 1.]]]]

    # np.ones((2,3,3,3))，2个里面嵌套3个，这3个又嵌套3个，接着后面三个里面又有3个1
    array2 = [[[[1., 1., 1.], [1., 1., 1.], [1., 1., 1.]], [[1., 1., 1.], [1., 1., 1.], [1., 1., 1.]],
               [[1., 1., 1.], [1., 1., 1.], [1., 1., 1.]]],
              [[[1., 1., 1.], [1., 1., 1.], [1., 1., 1.]], [[1., 1., 1.], [1., 1., 1.], [1., 1., 1.]],
               [[1., 1., 1.], [1., 1., 1.], [1., 1., 1.]]]]
