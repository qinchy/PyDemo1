import tushare as ts

if __name__ == '__main__':
    token = '32e73e8ad4c40ba77adebc92cad7d94147e78c4a82c5e49cdacdd2c9'
    pro = ts.pro_api(token)

    data = pro.query('stock_basic', exchange='', list_status='L',
                     fields='ts_code,symbol,name,area,industry,list_date')
    print(data)

    data = pro.daily(ts_code='000001.SZ', start_date='20230701', end_date='20240112')
    print(data)
