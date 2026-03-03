# 主入口函数

from corpus_loader import load_corpus
from index_builder import load_or_build_index
from poem_generator import generate_poem

def main():

    print("=== 隐写集句诗生成器 ===")
    hidden_text = input("请输入要隐写的一句话：").strip()
    m = int(input("请输入每句字数（5或7）："))
    a = int(input("请输入隐写位置 a："))
    b = int(input("请输入隐写位置 b："))

    if m not in (5, 7):
        raise ValueError("m 必须为 5 或 7")

    if a == b or a > m or b >= m:
        raise ValueError("a,b 必须不同，且 a <= m，b < m")

    corpus = load_corpus("chinese-poetry/全唐诗")
    index = load_or_build_index(corpus, m)
    poem = generate_poem(hidden_text, m, a, b, index)

    print("\n=== 生成结果 ===\n")
    for line in poem:
        print(line)

if __name__ == "__main__":
    main()