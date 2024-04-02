import re
import docx2txt
import pygraphviz as pgv

def extract_headings(text):
    """
    从文本中提取标题
    """
    pattern = re.compile(r'^(.+?)\s*$')
    headings = []
    for line in text.split('\n'):
        match = pattern.match(line)
        if match:
            headings.append(match.group(1))
    return headings

def generate_mind_map(headings):
    """
    根据标题生成思维导图
    """
    graph = pgv.AGraph(strict=True, directed=True)
    for i in range(len(headings) - 1):
        graph.add_node(headings[i])
        graph.add_node(headings[i + 1])
        graph.add_edge(headings[i], headings[i + 1])
    return graph

def save_mind_map(graph, output_path, format='png'):
    """
    将思维导图保存为图像文件
    """
    # 指定字体为支持中文的字体
    graph.node_attr['fontname'] = 'SimHei'
    graph.edge_attr['fontname'] = 'SimHei'

    graph.layout(prog='dot')
    graph.draw(output_path, format=format)

def word_to_mind_map(docx_path, output_path):
    """
    将Word文档转换为思维导图
    """
    text = docx2txt.process(docx_path)
    headings = extract_headings(text)
    graph = generate_mind_map(headings)
    save_mind_map(graph, output_path)

if __name__ == '__main__':
    # 示例用法
    word_to_mind_map('C:\\Users\\Administrator\\Downloads\\mytest.docx', 'C:\\Users\\Administrator\\Downloads\\output.png')
