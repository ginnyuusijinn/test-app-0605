import random

# 2文字姓・2文字名の候補（男性名のみ）
last_names = ['佐藤', '鈴木', '高橋', '田中', '渡辺', '伊藤', '山本', '中村', '小林', '加藤']
first_names = ['健太', '翔太', '大輔', '直樹', '悠斗', '優斗', '拓海', '海斗', '陽斗', '陸斗', '和也', '達也', '一樹', '和樹', '拓真']

# 漢数字リスト
kanji_numbers = ['一', '二', '三', '四', '五', '六', '七', '八', '九', '十']

def generate_name(i):
    ln = random.choice(last_names)
    fn = random.choice(first_names)
    kanji = kanji_numbers[i % len(kanji_numbers)]
    # 姓1文字＋漢数字＋姓2文字目＋名1文字目 で4文字にする
    name = ln[0] + kanji + ln[1] + fn[0]
    return name

def generate_time():
    return round(random.uniform(9.56, 12.99), 2)

athletes = []
for i in range(50):
    name = generate_name(i)
    time = generate_time()
    athletes.append({'name': name, 'time': time})

athletes_sorted = sorted(athletes, key=lambda x: x['time'])

for idx, athlete in enumerate(athletes_sorted, 1):
    print(f"{idx:2d}位: {athlete['name']} - {athlete['time']}秒")