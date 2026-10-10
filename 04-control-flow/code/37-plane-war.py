# 第 37 讲：小试牛刀 —— 飞机大战（有限回合、自动对打版）
# 原始代码用 pynput 监听键盘（需要装库、还要一直按键才能玩），
# 这里改成「有限回合、自动对打」的演示版：跑完自动退出，不会卡住。
# 直接运行：python3 37-plane-war.py

import random

random.seed(7)   # 固定随机种子，让每次运行结果一致

# 生成地图：3x3 网格，0 表示空位，"x" 表示我方飞机
background = [[0, 0, 0],
              [0, "x", 0],
              [0, 0, 0]]


def show_map():
    """打印当前地图。"""
    for row in background:
        print(row)
    print("-" * 12)


def find_player():
    """找到我方飞机当前坐标 (行, 列)，找不到返回 None。"""
    for i in range(3):
        for j in range(3):
            if background[i][j] == "x":
                return i, j
    return None


def move_player(direction):
    """按方向移动我方飞机，越过边界就不动。"""
    pos = find_player()
    if pos is None:
        return
    i, j = pos
    di, dj = direction
    ni, nj = i + di, j + dj
    if 0 <= ni < 3 and 0 <= nj < 3:
        background[i][j] = 0
        background[ni][nj] = "x"


# 敌机：每个敌机有名字和生命值
enemies = [
    {"name": "敌机A", "hp": 60},
    {"name": "敌机B", "hp": 40},
    {"name": "敌机C", "hp": 80},
]

player_hp = 100
moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]   # 右、左、下、上

print("=== 飞机大战（自动对打版）===")
show_map()

round_no = 0
max_rounds = 6
while player_hp > 0 and enemies and round_no < max_rounds:
    round_no += 1
    print(f"\n第 {round_no} 回合")

    # 我方随机移动并显示地图
    move_player(random.choice(moves))
    show_map()

    # 我方开火，攻击当前目标敌机
    enemy = enemies[0]
    damage = random.randint(10, 30)
    enemy["hp"] -= damage
    print(f"我方开火，{enemy['name']} 受到 {damage} 点伤害，剩余生命值 {max(enemy['hp'], 0)}")
    if enemy["hp"] <= 0:
        print(f"{enemy['name']} 被击落！")
        enemies.pop(0)

    # 敌机反击
    if enemies:
        counter = random.randint(5, 20)
        player_hp -= counter
        print(f"敌机反击，我方受到 {counter} 点伤害，剩余生命值 {max(player_hp, 0)}")

print("\n=== 战斗结束 ===")
if player_hp <= 0:
    print("我方飞机被击落，游戏结束")
elif not enemies:
    print("敌机全部被击落，我方胜利！")
else:
    print(f"到达回合上限({max_rounds})，战斗中止。我方剩余生命值 {max(player_hp, 0)}")


# 课后作业演示：用 +、- 符号恢复 / 扣除血量，血量为 0 时游戏结束
# 交互按键无法在文档里演示，这里用固定按键序列代替键盘输入
print("\n=== 课后作业：血量增减演示 ===")
hp = 100
keys = ["+", "-", "+", "-", "-", "-"]   # 相当于用户依次按下的键
for key in keys:
    if key == "+":
        delta = random.randint(1, 100)
        hp = min(100, hp + delta)   # 最大血量 100
        print(f"按下 +，恢复 {delta} 点，当前血量 {hp}")
    else:
        delta = random.randint(1, 100)
        hp -= delta
        print(f"按下 -，扣除 {delta} 点，当前血量 {max(hp, 0)}")
    if hp <= 0:
        print("血量为 0，游戏结束")
        break
