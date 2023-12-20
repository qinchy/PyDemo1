import sys
from os.path import dirname, abspath, split

if __name__ == '__main__':
    # __file__ 是当前文件的路径
    print(__file__)
    print(dirname(__file__))
    print(abspath(__file__))

    print(sys.path)
    sys.path.insert(0, abspath(dirname(abspath(__file__)) + '/..'))
    print(sys.path)

    curPath = abspath(dirname(__file__))
    print(curPath)

    rootPath = split(curPath)[0]
    print(rootPath)

    sys.path.append(split(rootPath)[0])
    print(sys.path)
