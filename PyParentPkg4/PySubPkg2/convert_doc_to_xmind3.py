import re
from docx import Document
import pygraphviz as pgv

def extract_headings(docx_path):
    """
    从Word文档中提取标题和层次
    """
    doc = Document(docx_path)
    headings = []
    for paragraph in doc.paragraphs:
        if paragraph.style.name.startswith('Heading'):
            level = int(paragraph.style.name.split()[1])
            title = paragraph.text.strip()
            headings.append((level, title))
    return headings

def generate_mind_map(headings):
    """
    根据标题生成思维导图
    """
    graph = pgv.AGraph(strict=True, directed=True)
    last_node = {1: None}
    for level, title in headings:
        graph.add_node(title)
        if level > 1:
            parent_title = last_node[level - 1]
            graph.add_edge(parent_title, title)
        last_node[level] = title
    return graph

def save_mind_map(graph, output_path, format='png'):
    """
    将思维导图保存为图像文件
    """
    # 设置全局字体为中文字体
    # 指定字体为支持中文的字体
    graph.node_attr['fontname'] = 'SimHei'
    graph.edge_attr['fontname'] = 'SimHei'
    graph.layout(prog='dot')
    graph.draw(output_path, format=format)

def word_to_mind_map(docx_path, output_path):
    """
    将Word文档转换为思维导图
    """
    headings = extract_headings(docx_path)
    graph = generate_mind_map(headings)
    save_mind_map(graph, output_path)

if __name__ == '__main__':
    # 示例用法
    word_to_mind_map('C:\\Users\\Administrator\\Downloads\\mytest.docx', 'C:\\Users\\Administrator\\Downloads\\output.png')
