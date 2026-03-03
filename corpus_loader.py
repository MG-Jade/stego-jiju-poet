# 语料加载

import os
import json
import re
from zhconv import convert
from utils import clean_line

def load_corpus(folder_path):

    corpus = {5: [], 7: []}
    pattern = re.compile(r"^poet\.(tang|song)\.\d+\.json$")

    for file in os.listdir(folder_path):

        if not pattern.match(file):
            continue

        full_path = os.path.join(folder_path, file)

        with open(full_path, encoding="utf-8") as f:
            data = json.load(f)

        for poem in data:
            for raw_line in poem.get("paragraphs", []):

                # 按标点拆分
                parts = re.split(r"[，。！？]", raw_line)

                for part in parts:
                    line = convert(part, "zh-hans")
                    line = clean_line(line)

                    if len(line) in (5, 7):
                        corpus[len(line)].append(line)

    return corpus