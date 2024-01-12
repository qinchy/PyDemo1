import tushare as ts

if __name__ == '__main__':
    token = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
    pro = ts.pro_api(token)

    data = pro.query('stock_basic', exchange='', list_status='L',
                     fields='ts_code,symbol,name,area,industry,list_date')
    print(data)

    data = pro.daily(ts_code='000001.SZ', start_date='20230701', end_date='20240112')
    print(data)
