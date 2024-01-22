import pandas as pd
import yfinance as yf

if __name__ == '__main__':
    symbol = "600519.SS"
    moutai_data = yf.download(symbol, start="2024-01-01", end="2024-01-12", proxy="127.0.0.1:7890")
    type(moutai_data)
    print(moutai_data)

    data_frame = pd.DataFrame(
        data=[{'Mango': 4, 'Apple': 5, 'Banana': 2},
              {'Mango': 5, 'Apple': 4, 'Banana': 3},
              {'Mango': 6, 'Apple': 3, 'Banana': 5},
              {'Mango': 3, 'Apple': 0, 'Banana': 2},
              {'Mango': 1, 'Apple': 2, 'Banana': 7},
              {'Mango': 8, 'Apple': 5, 'Banana': 6},
              {'Mango': 5, 'Apple': 1, 'Banana': 8}
              ], dtype=(str, int))
    print(data_frame)

    data_frame = pd.DataFrame(
        data={'Mango': [4, 5, 6, 3, 1], 'Apple': [5, 4, 3, 0, 2], 'Banana': [2, 3, 5, 2, 7]}, dtype=(str, list))
    print(data_frame)
