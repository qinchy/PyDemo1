# 导入urllib库的urlopen函数
import base64
from urllib.request import urlopen, urlretrieve

# 导入BeautifulSoup
from bs4 import BeautifulSoup as bf


# 获取title
def get_title(obj):
    # 从标签head、title里提取标题
    title = obj.head.title

    # 打印标题
    print(title)


# 获取当前网页下面所有img节点
def get_images(obj):
    # 使用find_all函数获取所有图片的信息
    pic_info = obj.find_all('img')
    # 分别打印每个图片的信息
    for i in pic_info:
        logo_url = i['src']
        # 包含base64的场景
        if logo_url.find("base64") > 0:
            image_base64 = logo_url[logo_url.rindex("base64,") + 7:]
            image_base64 = image_base64 + "="
            print(type(image_base64))
            # 解码图片
            imgdata = base64.b64decode(image_base64)
            # 将图片保存为文件
            with open("temp.jpg", 'wb') as f:
                f.write(imgdata)

            # 如果是base64编码的图片，直接写文件后执行下一次循环
            continue

        # 除了上述base64之外，其他不带http的场景
        if not logo_url.startswith("https:"):
            logo_url = "https:" + logo_url

        # 打印链接
        print(logo_url)
        # 使用urlretrieve下载图片
        urlretrieve(logo_url, logo_url[logo_url.rindex("/"):])


if __name__ == '__main__':
    # 发出请求，获取html
    html = urlopen("http://www.baidu.com/")

    # 用BeautifulSoup解析html
    obj = bf(html.read(), 'html.parser')

    # 打印 title
    get_title(obj)

    # 打印所有img节点
    get_images(obj)
