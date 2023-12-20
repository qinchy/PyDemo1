import sys

# while True:
#     try:
#         x = int(input("请输入一个数字: "))
#         break
#     except ValueError:
#         print("您输入的不是数字，请再次尝试输入！")

try:
    f = open('/tmp/foo.txt', 'r+')
    # print(f.encoding)
    s = f.readline()
    # print(s)
    # i = int(s.strip())
    i = int(5/0)
except OSError as err:
    print("OS error: {0}".format(err))
except ValueError:
    print("Could not convert data to an integer.")
except ZeroDivisionError:
    print("ZeroDivisionError: division by zero.")
except:
    print("Unexpected error:", sys.exc_info()[0])
    raise

# MyError的基类是Exception
class MyError(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)

try:
    raise MyError(2*2)
except MyError as e:
    print('My exception occurred, value:', e.value)

class Error(Exception):
    """
    Base class for exceptions in this module.
    """
    pass

class InputError(Error):
    """
    Exception raised for errors in the input.

    Attributes:
        expression -- input expression in which the error occurred
        message -- explanation of the error
    """

    def __init__(self, expression, message):
        self.expression = expression
        self.message = message

class TransitionError(Error):
    """
    Raised when an operation attempts a state transition that's not allowed.

    Attributes:
        previous -- state at beginning of transition
        next -- attempted new state
        message -- explanation of why the specific transition is not allowed
    """

    def __init__(self, previous, next, message):
        self.previous = previous
        self.next = next
        self.message = message

try:
    x = int(input("请输入一个数字: "))
    raise InputError("x", "输入错误")
except InputError as e:
    print('InputError exception occurred, variable {0}, value {1}'.format(e.expression, e.message))
except ValueError as e:
    print('InputError exception occurred, cause {0}', e.__cause__)