import numpy as np

if __name__ == '__main__':
    list = np.eye(6);
    print(list)

    print("打印一维数组")
    a = np.array([1, 2, 3])
    print(a)

    print("打印二维数组")
    a = np.array([[1, 2], [3, 4]])
    print(a)

    print("打印三维数组")
    a = np.array([[[1, 2, 3], [1, 2, 3], [1, 2, 3]], [[1, 2, 3], [1, 2, 3], [1, 2, 3]]])
    print(a)

    a = np.array([1, 2, 3, 4, 5], ndmin=3)
    print(a)

    a = np.array([1, 2, 3], dtype=complex, ndmin=3)
    print(a)

    dt = np.dtype(np.int32)
    print(dt)

    dt = np.dtype('i4')
    print(dt)

    # 字节顺序标注
    dt = np.dtype('<i4')
    print(dt)

    dt = np.dtype([('age', np.int8)])
    a = np.array([(10,), (20,), (30,)], dtype=dt)
    print(a)
