import random

if __name__ == '__main__':
    print("==获取[0-1]中的一个浮点数==")
    for i in range(10):
        float_between_0_and_1 = random.random()
        print(float_between_0_and_1, type(float_between_0_and_1))

    # 从列表中随机取一个
    print("==获取列表[5, 96, 52, 46, 47, 56, 79, 96]中的一个数==")
    for i in range(10):
        choice_item_value = random.choice([5, 96, 52, 46, 47, 56, 79, 96])
        print(choice_item_value, type(choice_item_value))

    # 获取[0-100]之间的数
    print("==获取[0-100]之间的数==")
    for i in range(10):
        random_range_between_0_and_100 = random.randrange(0, 100)
        print(random_range_between_0_and_100, type(random_range_between_0_and_100))

    # 获取[5-10]之间的整数，包含起始和终止
    print("==获取[5-10]之间的整数==")
    for i in range(10):
        random_between_5_and_10 = random.randint(5, 10)
        print(random_between_5_and_10, type(random_between_5_and_10))
