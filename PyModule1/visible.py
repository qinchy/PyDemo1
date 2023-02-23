# =====================================================
# 局部（在sum函数中未用global关键字修饰total）
total = 0 # 这是一个全局变量

# 可写函数说明
def sum( arg1, arg2 ):
    #返回2个参数的和."
    total = arg1 + arg2 # total在这里是局部变量.
    print ("函数内是局部变量 : ", total)
    return total
 
#调用sum函数
sum( 10, 20 )
print ("函数外是全局变量 : ", total)

# =====================================================
# 全局
num = 1
def fun1():
    global num  # 需要使用 global 关键字声明
    print(num) 
    num = 123
    print(num)

fun1()
print(num)


# =====================================================
# 闭包
def outer():
    num = 10
    def inner():
        nonlocal num   # nonlocal关键字声明闭包作用域
        num = 100
        print(num)
    inner()

    print(num)

outer()