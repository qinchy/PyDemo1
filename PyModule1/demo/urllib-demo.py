import urllib.parse
import urllib.request
import urllib.robotparser

if __name__ == '__main__':
    try:
        myURL = urllib.request.urlopen("https://www.runoob.com/")
    except urllib.error.HTTPError as e:
        if e.code == 404:
            print(404)  # 404
            raise

    print("响应码：%s" % myURL.getcode())

    # print(myURL.read())
    lines = myURL.readlines()
    for line in lines:
        print(line)

    print("================request with header================")

    url = 'https://www.runoob.com/?s='  # 菜鸟教程搜索页面
    keyword = 'Python 教程'
    key_code = urllib.request.quote(keyword)  # 对请求进行编码
    url_all = url + key_code
    header = {
        'User-Agent': 'Mozilla/5.0 (X11; Fedora; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}  # 头部信息
    request = urllib.request.Request(url_all, headers=header)
    reponse = urllib.request.urlopen(request).read()

    fh = open("./urllib_test_runoob_search.html", "wb")  # 将文件写入到当前目录中
    fh.write(reponse)
    fh.close()

    print("============request with data using post============")

    url = 'https://www.runoob.com/try/py3/py3_urllib_test.php'  # 提交到表单页面
    data = {'name': 'RUNOOB', 'tag': '菜鸟教程'}  # 提交数据
    header = {
        'User-Agent': 'Mozilla/5.0 (X11; Fedora; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}  # 头部信息
    data = urllib.parse.urlencode(data).encode('utf8')  # 对参数进行编码，解码使用 urllib.parse.urldecode
    request = urllib.request.Request(url, data, header)  # 请求处理
    reponse = urllib.request.urlopen(request).read()  # 读取结果

    fh = open("./urllib_test_post_runoob.html", "wb")  # 将文件写入到当前目录中
    fh.write(reponse)
    fh.close()

    print("==========url parse==========")
    o = urllib.parse.urlparse("https://www.runoob.com/?s=python+%E6%95%99%E7%A8%8B")
    print(o)

    print("==========parse robots.txt==========")
    rp = urllib.robotparser.RobotFileParser()
    # 设置 robots.txt 文件的 URL。
    rp.set_url("http://www.musi-cal.com/robots.txt")
    # 读取 robots.txt URL 并将其输入解析器。
    rp.read()

    # 以 named tuple RequestRate(requests, seconds) 的形式从 robots.txt 返回 Request-rate 形参的内容
    # 如果此形参不存在或不适用于指定的 useragent 或者此形参的 robots.txt 条目存在语法错误，则返回 None。
    rrate = rp.request_rate("*")
    print(rrate)
    # print("请求次数：%n"%rrate.requests)
    # print("请求频率：%n"%rrate.seconds)
    print(rp.crawl_delay("*"))

    # 如果允许 useragent 按照被解析 robots.txt 文件中的规则来获取 url 则返回 True。
    print(rp.can_fetch("*", "http://www.musi-cal.com/cgi-bin/search?city=San+Francisco"))
    print(rp.can_fetch("*", "http://www.musi-cal.com/"))
