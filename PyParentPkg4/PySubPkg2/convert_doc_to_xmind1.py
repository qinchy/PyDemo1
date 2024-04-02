import re
from docx import Document
import pygraphviz as pgv


def extract_text_from_docx(docx_path):
    """
    从Word文档中提取文本
    """
    doc = Document(docx_path)
    text = []
    for para in doc.paragraphs:
        text.append(para.text)
    return '\n'.join(text)


def generate_mind_map(text):
    """
    根据文本生成思维导图
    """
    graph = pgv.AGraph(strict=True, directed=True)
    nodes = set()
    edges = set()

    # 使用正则表达式查找可能的关键词或标题
    pattern = re.compile(r'^(.+?)\s*$')

    current_parent = None
    for line in text.split('\n'):
        match = pattern.match(line)
        if match:
            # 如果匹配到标题，则创建一个新节点作为父节点
            current_parent = match.group(1)
            graph.add_node(current_parent)
        elif current_parent:
            # 如果没有匹配到标题，则将文本添加为当前父节点的子节点
            child = line.strip()
            if child:
                graph.add_node(child)
                graph.add_edge(current_parent, child)

    return graph


def save_mind_map(graph, output_path, format='png'):
    """
    将思维导图保存为图像文件
    """
    graph.layout(prog='dot')
    graph.draw(output_path, format=format)


def word_to_mind_map(docx_path, output_path):
    """
    将Word文档转换为思维导图
    """
    text = extract_text_from_docx(docx_path)
    print(text)
    graph = generate_mind_map(text)
    print(graph)
    save_mind_map(graph, output_path)

if __name__ == '__main__':
    # 示例用法
    word_to_mind_map('C:\\Users\\Administrator\\Downloads\\货币桥报文20220401_v21.docx', 'C:\\Users\\Administrator\\Downloads\\output.png')
