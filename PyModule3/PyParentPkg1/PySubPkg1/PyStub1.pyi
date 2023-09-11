# 约束使用该方法的限制，有点类似于只有接口没有实现
# 约定传入的参数必须是string，方法返回值也必须是string
# 后面...表示实现接口的方法体
def greeting(name: str) -> str: ...