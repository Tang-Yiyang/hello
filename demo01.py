# ============================================
# 第 1 课 · 配套示例（讲义里每一段代码都在这里）
# 跑法：VS Code 里按 F5，或者终端 python3 demo01.py
# 用法：读到讲义某一段，就来这里找同编号的部分，看真实输出
# 注意：这个文件不用你改，跑就完事
# ============================================


def line(title):
    print()
    print("=" * 52)
    print(title)
    print("=" * 52)


# --------------------------------------------------
line("1. 变量就是给数据起个名字")

age = 18
name = "Tang Ian"
print("age  =", age)
print("name =", name)

# 变量可以重新赋值，后写的覆盖先写的
score = 60
print("一开始 score =", score)
score = 95
print("重新赋值后 score =", score)

# 右边先用旧的自己算出新值
score = score + 5
print("score = score + 5 之后 =", score)


# --------------------------------------------------
line("2. 变量名能不能用这些？（合法的写法）")

my_age = 18
myAge = 18
_my_age = 18
my_age2 = 18
年龄 = 18                      # 中文能用，但工程里别用
print("以上全都能跑：", my_age, myAge, _my_age, my_age2, 年龄)


# --------------------------------------------------
line("3. 四种基本类型")

n = 18                  # int   整数
f = 1.75                # float 小数
s = "Tang Ian"          # str   字符串
b = True                # bool  布尔
print("n =", n, " 类型:", type(n))
print("f =", f, " 类型:", type(f))
print("s =", s, " 类型:", type(s))
print("b =", b, " 类型:", type(b))


# --------------------------------------------------
line("4. 整数 int：除法会变小数，整除用 //")

print("7 + 3  =", 7 + 3)
print("7 - 3  =", 7 - 3)
print("7 * 3  =", 7 * 3)
print("7 / 3  =", 7 / 3, "   <- 一个斜杠，结果一定是小数")
print("7 // 3 =", 7 // 3, "  <- 两个斜杠，整除，只留整数部分")
print("7 % 3  =", 7 % 3, "   <- 取余数")
print("2 ** 10 =", 2 ** 10, " <- 乘方，2 的 10 次方")
print("1000000 可以写成 1_000_000 =", 1_000_000)


# --------------------------------------------------
line("5. 浮点数 float：小数不是精确的（必看）")

print("0.1 + 0.2 =", 0.1 + 0.2)
print("0.1 + 0.2 == 0.3 ?", 0.1 + 0.2 == 0.3)
print("这不是 Python 的 bug，是所有语言的通病（二进制存不下 0.1）")
print("比较小数时一般这样写：abs((0.1+0.2) - 0.3) < 1e-9 ->",
      abs((0.1 + 0.2) - 0.3) < 1e-9)


# --------------------------------------------------
line("6. 字符串 str：单引号双引号都行")

a = "Tang Ian"
b = 'Tang Ian'
print("双引号:", a)
print("单引号:", b)
print("两者相等吗:", a == b)

# 引号里面套引号
quote = "他说：'你好'"
quote2 = '他说："你好"'
print(quote)
print(quote2)

# 转义：\n 换行，\t 制表符
print("第一行\n第二行")
print("名字\t分数")
print("长度 len('Tang Ian') =", len("Tang Ian"))


# --------------------------------------------------
line("7. 布尔 bool：只有 True 和 False")

is_student = True
has_job = False
print("is_student =", is_student)
print("has_job    =", has_job)
print("True 的类型:", type(True))
print("1 + True  =", 1 + True, "   <- True 其实就是 1")
print("1 + False =", 1 + False, "  <- False 就是 0")


# --------------------------------------------------
line("8. type()：随时问 Python 这是什么类型")

print(type(18))
print(type(1.75))
print(type("18"))
print(type(True))
print("注意区别：18 和 \"18\" 是两个完全不同的东西")
print("  18 的类型:", type(18))
print("  \"18\" 的类型:", type("18"))


# --------------------------------------------------
line("9. 类型转换：把一种类型变成另一种")

print("int('18')   =", int("18"), "  字符串 -> 整数")
print("float('18') =", float("18"), " 字符串 -> 小数")
print("str(18)     =", repr(str(18)), " 整数 -> 字符串")
print("int(1.99)   =", int(1.99), "  小数 -> 整数（直接砍掉小数，不是四舍五入）")
print("round(1.99) =", round(1.99), " 这个才是四舍五入")

# 转不了的会报错
print("--- 下面故意报错，看报错长什么样 ---")
try:
    int("abc")
except ValueError as e:
    print("报错 ->", type(e).__name__, ":", e)

print("--- bool() 转一切 ---")
print("bool(0)     =", bool(0))
print("bool(1)     =", bool(1))
print("bool(-5)    =", bool(-5))
print("bool('')    =", bool(""))
print("bool('abc') =", bool("abc"))
print("bool(None)  =", bool(None))


# --------------------------------------------------
line("10. 字符串相加 vs 数字相加（新手第一大坑）")

print("'3' + '4' =", "3" + "4", "   <- 字符串相加是拼接")
print("3 + 4     =", 3 + 4, "       <- 数字相加才是算数")

print("--- 下面这个一定报错 ---")
try:
    print("温度是 " + 25)
except TypeError as e:
    print("报错 ->", type(e).__name__, ":", e)
print("正确写法1：", "温度是 " + str(25))
print("正确写法2：", f"温度是 {25}", "  <- f-string，推荐")


# --------------------------------------------------
line("11. f-string：把变量塞进句子里（最常用）")

name = "Tang Ian"
age = 18
print("普通写法:", "Hello, " + name + "! You are " + str(age + 1) + " next year.")
print("f-string :", f"Hello, {name}! You are {age + 1} next year.")
print("花括号里可以放变量、也可以放算式:", f"{name} 的年龄乘以 2 是 {age * 2}")
print("格式控制（保留 2 位小数）:", f"{3.1415926:.2f}")
print("百分比:", f"{0.876:.1%}")


# --------------------------------------------------
line("12. 比较运算符：结果一定是布尔")

age = 18
print("18 >= 18  ->", age >= 18)
print("18 >  18  ->", age > 18)
print("18 == 18  ->", age == 18)
print("18 != 18  ->", age != 18)
print("注意: 判断相等是两个等号 ==，一个等号是赋值")
print("'Tang' in 'Tang Ian' ->", "Tang" in "Tang Ian")


# --------------------------------------------------
line("13. if / elif / else：让程序选一条路走")

score = 85

if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 60:
    print("C")
else:
    print("不及格")

print("--- 再看一个只有两条路的 ---")
is_student = True
if is_student:
    print("你是学生，可以买学生票")
else:
    print("全价")


# --------------------------------------------------
line("14. 逻辑运算：and / or / not")

age = 18
has_id = True

print("age >= 18 and has_id  ->", age >= 18 and has_id, " 两个都真才真")
print("age > 30   or  has_id  ->", age > 30 or has_id, " 有一个真就真")
print("not has_id             ->", not has_id, "         取反")

if age >= 18 and has_id:
    print("→ 可以进")


# --------------------------------------------------
line("15. 复合赋值：+= 一大家子")

x = 20
x += 5
print("20 += 5   ->", x)
x -= 3
print("25 -= 3   ->", x)
x *= 2
print("22 *= 2   ->", x)
x //= 4
print("44 //= 4  ->", x)
x **= 2
print("11 **= 2  ->", x)
x %= 5
print("121 %= 5  ->", x)


# --------------------------------------------------
line("16. += 在列表和字符串上（和第 2 课衔接）")

s = "第"
s += "1"
s += "课"
print("字符串拼接:", s)

nums = [1, 2]
nums += [3, 4]
print("列表 += :", nums, "  <- 拆开逐个加进去")

nums2 = [1, 2]
nums2.append([3, 4])
print("append  :", nums2, "  <- 把整个列表当一个元素")


# --------------------------------------------------
line("全部示例跑完 —— 现在可以去看第 1 课练习了")
