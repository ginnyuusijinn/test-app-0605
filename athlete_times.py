import random

# 2文字姓・2文字名の候補（男性名のみ）
last_names = ['佐藤', '鈴木', '高橋', '田中', '渡辺', '伊藤', '山本', '中村', '小林', '加藤']
first_names = ['健太', '翔太', '大輔', '直樹', '悠斗', '優斗', '拓海', '海斗', '陽斗', '陸斗', '和也', '達也', '一樹', '和樹', '拓真']

def generate_name():
    ln = random.choice(last_names)
    fn = random.choice(first_names)
    return ln + fn  # 四文字の実在するような男性名

def generate_time():
    return round(random.uniform(9.56, 12.99), 2)

athletes = []
for _ in range(50):
    name = generate_name()
    time = generate_time()
    athletes.append({'name': name, 'time': time})

athletes_sorted = sorted(athletes, key=lambda x: x['time'])

for idx, athlete in enumerate(athletes_sorted, 1):
    print(f"{idx:2d}位: {athlete['name']} - {athlete['time']}秒")