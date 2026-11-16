# ============================================
# 第 2 课 · 配套示例（讲义里每一段代码都在这里）
# 跑法：VS Code 里按 F5，或者终端 python3 demo02.py
# 用法：一边读讲义一边跑这个文件，输出对得上就说明你懂了
# 注意：这个文件不用你改，跑就完事
# ============================================


def line(title):
    print()
    print("=" * 52)
    print(title)
    print("=" * 52)


# --------------------------------------------------
line("1. 列表长什么样")

nums = [3, 7, 1, 9]
names = ["Tang Ian", "Xiao Ming", "Li Hua"]
mixed = [18, "Tang Ian", 1.75, True]    # 类型可以混装
empty = []                              # 空列表

print("nums  =", nums)
print("names =", names)
print("mixed =", mixed)
print("empty =", empty)
print("nums 的类型是:", type(nums))


# --------------------------------------------------
line("2. 取元素：索引从 0 开始")

nums = [3, 7, 1, 9]
print("nums      =", nums)
print("nums[0]   =", nums[0], "  <- 第一个")
print("nums[1]   =", nums[1], "  <- 第二个")
print("nums[3]   =", nums[3], "  <- 最后一个")
print("nums[-1]  =", nums[-1], "  <- 倒数第一个，负号从右边数")
print("nums[-2]  =", nums[-2], "  <- 倒数第二个")


# --------------------------------------------------
line("3. 越界会报错（这是故意写的，看报错长什么样）")

nums = [3, 7, 1, 9]
print("列表只有 4 个元素，下标最大是 3")
try:
    print(nums[4])
except IndexError as e:
    print("报错了 ->", type(e).__name__, ":", e)


# --------------------------------------------------
line("4. 改元素：直接给它赋值")

nums = [3, 7, 1, 9]
print("改之前:", nums)
nums[0] = 100
print("nums[0] = 100 之后:", nums)


# --------------------------------------------------
line("5. 有多长：len()")

nums = [3, 7, 1, 9]
print("nums =", nums)
print("len(nums) =", len(nums))


# --------------------------------------------------
line("6. 加元素：append 加到末尾，insert 插到指定位置")

nums = [3, 7, 1, 9]
print("原始      :", nums)
nums.append(100)
print("append(100):", nums)
nums.insert(0, 999)
print("insert(0,999):", nums, "  <- 插到最前面了")


# --------------------------------------------------
line("7. append 的坑：千万不要写成 nums = nums.append(...)")

nums = [1, 2, 3]
print("正常写法之前:", nums)
nums.append(4)
print("nums.append(4) 之后:", nums)

bad = [1, 2, 3]
result = bad.append(4)
print("result = bad.append(4) 时，result 是:", result, "  <- None！")
print("而 bad 本身其实已经变了:", bad)


# --------------------------------------------------
line("8. 删元素：remove 按值删，pop 按位置删")

nums = [3, 7, 1, 9]
print("原始        :", nums)
nums.remove(7)
print("remove(7) 后:", nums)

nums = [3, 7, 1, 9]
got = nums.pop(0)
print("pop(0) 后   :", nums, " 被弹出来的是:", got)


# --------------------------------------------------
line("9. 排序：sort 直接改自己，sorted 返回新的")

nums = [3, 7, 1, 9]
print("原始        :", nums)
nums.sort()
print("sort() 之后 :", nums)

nums = [3, 7, 1, 9]
new = sorted(nums)
print("sorted(nums):", new, " 而原列表没变:", nums)


# --------------------------------------------------
line("10. for 循环：一个一个取出来")

names = ["Tang Ian", "Xiao Ming", "Li Hua"]
for n in names:
    print("你好，", n)

print("--- 循环结束，这一行在循环外面（没有缩进）---")


# --------------------------------------------------
line("11. for + 列表：把每个数乘 2")

nums = [3, 7, 1, 9]
for n in nums:
    print(n, "乘以 2 是", n * 2)


# --------------------------------------------------
line("12. range：不想手写一堆数的时候")

print("range(5) 里的数是：")
for i in range(5):
    print(" ", i)

print("range(1, 6) 里的数是：")
for i in range(1, 6):
    print(" ", i, end="")
print()


# --------------------------------------------------
line("13. 累加模式（求和的标准骨架）")

nums = [3, 7, 1, 9]

total = 0               # ① 累加器，放在循环【外面】，一开始是 0
for n in nums:          # ② 一个一个取
    total += n          # ③ 累加：total = total + n
    print(f"   拿到 {n}，total 变成 {total}")

print("最终 total =", total)


# --------------------------------------------------
line("14. 如果累加器放错位置会怎样（这是新手最常犯的错）")

nums = [3, 7, 1, 9]

for n in nums:
    total = 0           # ❌ 放循环里面了，每一圈都被清零
    total += n
    print(f"   拿到 {n}，total 变成 {total}")
print("最终 total =", total, "  <- 只有 9，前三个白算了")


# --------------------------------------------------
line("15. 循环里同时用两个变量：zip")

names = ["Tang Ian", "Xiao Ming"]
scores = [92, 78]
for name, score in zip(names, scores):
    print(f"   {name} 考了 {score} 分")


# --------------------------------------------------
line("全部示例跑完 —— 现在可以去看练习题了")
