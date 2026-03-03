# 拼音相关

from pypinyin import pinyin, Style

def get_initial_final(char):
    initial = pinyin(char, style=Style.INITIALS, strict=False)[0][0]
    final = pinyin(char, style=Style.FINALS, strict=False)[0][0]
    return initial, final