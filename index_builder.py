# 索引构建

from collections import defaultdict
from pinyin_utils import get_initial_final
from config import get_rhyme_group
import pickle
import os

def build_index(lines, m):

    index = defaultdict(list)

    for line in lines:

        chars_info = []

        for ch in line:
            initial, final = get_initial_final(ch)
            chars_info.append({
                "char": ch,
                "initial": initial,
                "final": final,
                "rhyme": get_rhyme_group(final)
            })

        for a in range(m):
            for b in range(m):
                if a == b:
                    continue

                key = (
                    a,
                    chars_info[a]["initial"],
                    b,
                    chars_info[b]["final"]
                )

                index[key].append({
                    "text": line,
                    "chars": chars_info
                })

    return index

def load_or_build_index(corpus, m):

    os.makedirs("cache", exist_ok=True)
    cache_file = os.path.join("cache", f"index_m{m}.pkl")

    if os.path.exists(cache_file):
        print("发现缓存索引，正在加载...")
        with open(cache_file, "rb") as f:
            return pickle.load(f)

    print("未发现缓存，正在建立索引（首次较慢）...")
    index = build_index(corpus[m], m)

    print("保存索引缓存...")
    with open(cache_file, "wb") as f:
        pickle.dump(index, f, protocol=pickle.HIGHEST_PROTOCOL)

    return index