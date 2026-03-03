# 通用函数

def clean_line(line):
    return ''.join(c for c in line if '\u4e00' <= c <= '\u9fff')