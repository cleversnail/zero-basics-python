# 第 63 讲 · 避坑指南（2）：staticmethod 里误用了 self
# ⚠️ 本文件故意触发错误，用来演示真实报错：NameError
class Coffee:
    @staticmethod
    def make():
        # 错误：staticmethod 里既没有 self 也没有 cls，self 是不存在的名字
        print("制作", self.name)


Coffee.make()
