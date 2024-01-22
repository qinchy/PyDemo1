import datetime


class DatePrice:
    riqi: datetime.date
    price: float

    def __init__(self, riqi: datetime.date, price: float):
        self.riqi = riqi
        self.price = price

    def __str__(self):
        print(f"riqi:{self.riqi},price:{self.price}")


if __name__ == '__main__':
    data_base = datetime.date(2023, 12, 31)
    price_str = '30.14,20.98,16.65,56.16'
    price_array = price_str.split(',')
    data_array = list()

    for idx, price in enumerate(price_array):
        datePrice = DatePrice(data_base + datetime.timedelta(days=idx), price)
        data_array.append(datePrice)

    for datePrice in data_array:
        print("riqi=" + str(datePrice.riqi) + ",price=" + datePrice.price)
