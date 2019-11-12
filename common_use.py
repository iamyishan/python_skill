from collections import Counter

# 1.交换变量
a, b = 5, 10
print(a, b)
a, b = b, a
print(a, b)

# 2.统计列表中出现次数最多的那个数
a = [1, 2, 3, 1, 2, 3, 2, 2, 4, 5, 1]
# 方法1
print(set(a))
print(max(set(a), key=a.count))
# 方法2
cnt = Counter(a)
print(cnt.most_common(4))  # 出现次数最多的前n个元素及其次数

# 检查两个字符串是不是由相同字母不同顺序组成


