# 用 pdb 调试程序：观察每一步的变量值
# 运行（手动交互）：python3 03-pdb-demo.py
# 运行（自动喂命令，便于演示）：printf 'n\nn\npp x\npp y\nc\n' | python3 03-pdb-demo.py
import pdb


def add(a, b):
    result = a + b
    return result


def main():
    x = 10
    y = 20
    pdb.set_trace()          # 执行到这里会暂停，进入 pdb 交互
    z = add(x, y)
    print(f"x + y = {z}")


if __name__ == "__main__":
    main()
