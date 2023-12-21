class TradeData:
    """交易数据超类"""
    symbol: str
    price: float
    direction: str
    volume: int

    def __init__(self, symbol: str, price: float, direction: str, volume: int):
        self.symbol = symbol
        self.price = price
        self.direction = direction
        self.volume = volume

    def __str__(self) -> str:
        return f"symbol = {self.symbol}, price = {self.price}, direction = {self.direction}, volume = {self.volume}"


class StockTradeData(TradeData):
    """股票交易数据"""
    size: int

    def __init__(self, symbol: str, price: float, direction: str, volume: int, size: int):
        super().__init__(symbol, price, direction, volume)
        self.size = size

    def __str__(self) -> str:
        return f"symbol = {self.symbol}, price = {self.price}, direction = {self.direction}, volume = {self.volume}, " \
               f"size = {self.size}"


if __name__ == '__main__':
    stockTradeData = StockTradeData('600889', 10.23, 'BUY', 100, 1)
    print(stockTradeData)
