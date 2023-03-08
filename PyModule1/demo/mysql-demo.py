import mysql.connector

if __name__ == '__main__':
    mydb = mysql.connector.connect(
        host="localhost",  # 数据库主机地址
        user="root",  # 数据库用户名
        passwd="admin",  # 数据库密码
        database="sys"
    )

    # print(mydb)

    mycursor = mydb.cursor()

    mycursor.execute("select * from version")

    for x in mycursor:
        print(x)
