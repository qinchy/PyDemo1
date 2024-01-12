import seaborn as sns
import matplotlib.pyplot as plt

if __name__ == '__main__':
    tips = sns.load_dataset("tips")
    # 创建散点图
    sns.scatterplot(x='day', y='total_bill', hue="sex", data=tips)
    plt.show()

    sns.barplot(x="day", y="total_bill", hue="sex", data=tips)
    plt.show()
