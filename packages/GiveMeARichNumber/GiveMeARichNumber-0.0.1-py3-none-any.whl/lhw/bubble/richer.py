import random

if __name__ == '__main__':
    # 定义布尔变量 a
    a = False
    # 创建一个空列表 b
    b = []
    c = []
    # 循环从 1 到 35，将每个数字添加到 b 列表中
    for i in range(1, 37):
        b.append(i)
    for i in range(0,5):
        x = random.choice(b)
        print(x, end=" ")
        b.remove(x)
    for i in range(1, 13):
        c.append(i)

    for i in range(0,2):
        x = random.choice(c)
        print(x, end=" ")
        c.remove(x)
