# 匿名函数


# 只有当函数只有一句话的时候，才能把函数写成一行
def add(x,y): return x + y

# 匿名函数
# Lambda 定义函数一般是一次性的
lambda_add = lambda x, y:x + y

print(add(4, 5))
print(lambda_add(4, 5))
