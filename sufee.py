from hiraganautil import hiraganautil

hiragana_all = "あいうえおかきくけこさしすせそたちつてとなにぬねのはひふへほまみむめもやゆよらりるれろわをん"
#  ----------------------ここを弄る------------------------------------
shieldbreaker_onhand = "んうと"  # 手持ちのシールドブレーカー持ちの頭文字
changeguard_onhand = "きうゆかこ"  # 手持ちのチェンジガード持ちの頭文字
other_onhand = hiragana_all  # 手持ちのその他の頭文字
# other_onhand = "ふ"  # 手持ちのその他の頭文字
#  ----------------------ここまでを弄る------------------------------------
all_onhand = "".join([shieldbreaker_onhand, changeguard_onhand, other_onhand])


def word2plane(word):
    chars = [hiraganautil.hiragana2plane(char) for char in word]
    return "".join(chars)


def filtering_words(words):
    def check_shieldbreaker(word):
        return word[-1] in shieldbreaker_onhand

    def check_changeguard(word):
        has_second = word[-2] in changeguard_onhand
        has_third = word[-3] in changeguard_onhand
        return has_second and has_third

    def check_onhand(word):
        return all([char in all_onhand for char in word])

    return [word for word in words if check_shieldbreaker(word) and check_changeguard(word) and check_onhand(word)]


if __name__ == "__main__":
    syou = hiraganautil.load_words("data/syou.txt")
    chou = hiraganautil.load_words("data/chou.txt")
    jyou = hiraganautil.load_words("data/jyou.txt")
    hyou = hiraganautil.load_words("data/hyou.txt")
    syo = hiraganautil.load_words("data/syo.txt")
    cho = hiraganautil.load_words("data/cho.txt")
    jyo = hiraganautil.load_words("data/jyo.txt")
    hyo = hiraganautil.load_words("data/hyo.txt")

    syou = filtering_words(syou)
    chou = filtering_words(chou)
    jyou = filtering_words(jyou)
    hyou = filtering_words(hyou)
    syo= filtering_words(syo)
    cho= filtering_words(cho)
    jyo= filtering_words(jyo)
    hyo= filtering_words(hyo)

    print("----しょう")
    print(syou)
    print("----しょ")
    print(syo)
    print()

    print("----ちょう")
    print(chou)
    print("----ちょ")
    print(cho)
    print()

    print("----じょう")
    print(jyou)
    print("----じょ")
    print(jyo)
    print()

    print("----ひょう")
    print(hyou)
    print("----ひょ")
    print(hyo)
    print()
