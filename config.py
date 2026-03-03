# 中华新韵十四韵映射
NEW_RHYME_MAP = {

    # 一麻
    "a": 1, "ia": 1, "ua": 1,

    # 二波
    "o": 2, "e": 2, "uo": 2,

    # 三皆
    "ie": 3, "ue": 3,"ve": 3,

    # 四开
    "ai": 4, "uai": 4,

    # 五微
    "ei": 5, "ui": 5,

    # 六豪
    "ao": 6, "iao": 6,

    # 七尤
    "ou": 7, "iu": 7,

    # 八寒
    "an": 8, "ian": 8, "uan": 8, "van": 8,

    # 九文
    "en": 9, "in": 9, "un": 9, "vn": 9,

    # 十唐
    "ang": 10, "iang": 10, "uang": 10,

    # 十一庚
    "eng": 11, "ing": 11, "ong": 11, "iong": 11,

    # 十二齐
    "i": 12, "er": 12, "v": 12,

    # 十三支
    # 因为懒得区分所以和十二齐合并了

    # 十四姑
    "u": 14,
}


def get_rhyme_group(final):
    return NEW_RHYME_MAP.get(final)