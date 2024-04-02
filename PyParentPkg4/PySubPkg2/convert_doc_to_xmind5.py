import requests
import re
import pygraphviz as pgv
from bs4 import BeautifulSoup

def extract_headings_from_html(html_content):
    """
    从HTML内容中提取标题和层次
    """
    soup = BeautifulSoup(html_content, 'html.parser')
    headings = []
    for element in soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6']):
        level = int(element.name[1])
        title = element.get_text().strip()
        headings.append((level, title))
    return headings

def generate_mind_map(headings):
    """
    根据标题生成思维导图
    """
    graph = pgv.AGraph(strict=True, directed=True)
    last_node = {1: None}
    for level, title in headings:
        if level == 1:
            graph.add_node(title)
            last_node[1] = title
        else:
            parent_title = last_node[level - 1]
            graph.add_node(title)
            graph.add_edge(parent_title, title)
            last_node[level] = title
    return graph

def save_mind_map(graph, output_path, format='png'):
    """
    将思维导图保存为图像文件
    """
    graph.layout(prog='dot')
    graph.draw(output_path, format=format)

def fly_to_mind_map(doc_url, output_path):
    """
    将飞书在线文档转换为思维导图
    """
    response = requests.get(doc_url)
    if response.status_code == 200:
        html_content = response.text
        headings = extract_headings_from_html(html_content)
        graph = generate_mind_map(headings)
        save_mind_map(graph, output_path)
    else:
        print("Failed to download document")

# 示例用法
fly_to_mind_map('https://n515v0qvbn.feishu.cn/docs/doccnwdZj7aobg8IeYrpzQN6xih', 'output.png')
