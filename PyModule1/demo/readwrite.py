def write(file, model, content):
    # 写文件
    with open(file, model) as out_file:
        out_file.write(content)

def read(file, model): 
    # Read a file
    with open(file, model) as in_file:
        text = in_file.read()
        return text

if __name__ == "__main__":
    file = "/tmp/test.txt"
    content = "该文本会写入到文件中\n看到我了吧！"
    write(file, "wt", content) 

    print(read(file, "rt"))

