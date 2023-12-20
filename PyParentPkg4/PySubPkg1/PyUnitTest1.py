import unittest

import PyStub1


class MyTestCase(unittest.TestCase):
    """MyTestCase是unitest.TestCase的派生类"""

    def test_something(self):
        self.assertEqual(PyStub1.greeting('jack'), 'Hellojack', '预测结果不一致')
        self.assertEqual(True, False)  # add assertion here


if __name__ == '__main__':
    unittest.main()
