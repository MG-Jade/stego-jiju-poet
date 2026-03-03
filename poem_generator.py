# 生成诗

import random
from pinyin_utils import get_initial_final

def generate_poem(hidden_text, m, a, b, index):

    poem = []
    n = len(hidden_text)
    i = 0

    while i < n:

        if i == n - 1:
            hidden_char = hidden_text[i]
            target_initial, target_final = get_initial_final(hidden_char)

            key = (a - 1, target_initial, b - 1, target_final)
            candidates = index.get(key, [])

            if not candidates:
                raise ValueError(f"无法为字 {hidden_char} 找到候选句")

            poem.append(random.choice(candidates)["text"])
            break

        char1 = hidden_text[i]
        char2 = hidden_text[i + 1]

        init1, fin1 = get_initial_final(char1)
        init2, fin2 = get_initial_final(char2)

        key1 = (a - 1, init1, b - 1, fin1)
        key2 = (a - 1, init2, b - 1, fin2)

        candidates1 = index.get(key1, [])
        candidates2 = index.get(key2, [])

        if not candidates1 or not candidates2:
            raise ValueError(f"字 {char1} 或 {char2} 无候选句")

        random.shuffle(candidates1)

        for cand1 in candidates1:
            rhyme1 = cand1["chars"][-1]["rhyme"]
            if rhyme1 is None:
                continue

            rhyme_candidates2 = [
                c for c in candidates2
                if c["chars"][-1]["rhyme"] == rhyme1
            ]

            if rhyme_candidates2:
                poem.append(cand1["text"])
                poem.append(random.choice(rhyme_candidates2)["text"])
                break
        else:
            raise ValueError(f"字对 {char1}{char2} 无法押韵")

        i += 2

    return poem