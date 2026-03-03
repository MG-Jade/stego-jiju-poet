# 语料加载

import os
import json
import re
from zhconv import convert
from utils import clean_line

def load_corpus(folder_path):

    corpus = {5: [], 7: []}
    pattern = re.compile(r"^poet\.(tang|song)\.\d+\.json$")

    files = os.listdir(folder_path)

    for file in files:

        if not pattern.match(file):
            continue

        full_path = os.path.join(folder_path, file)

        with open(full_path, encoding="utf-8") as f:
            data = json.load(f)

        for poem in data:
            for line in poem.get("paragraphs", []):

                line = convert(line, "zh-hans")
                line = clean_line(line)

                if len(line) in (5, 7):
                    corpus[len(line)].append(line)

    return corpus