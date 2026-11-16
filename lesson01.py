# ============================================
# 第 1 课：变量和类型
# 日期：2026-11-16  第 1 周第 1 天
# --------------------------------------------
# 怎么跑：
#   在 VS Code 里打开这个文件 → 按 F5
#   或者终端里：python3 ~/dev/hello/lesson01.py
#
# 规则：
#   1. 只改写着 TODO 的那几行，变量名一个字都别动
#   2. 每个 TODO 删掉，换成你自己的值
#   3. 改完运行，先自己看输出对不对，再跑 check01.py 打分
# ============================================


# --- 任务 1：整数 int ---
# 把 age 写成你的年龄，直接写数字，不要引号
age = 18


# --- 任务 2：字符串 str ---
# 把 name 写成你的英文名，必须带引号（单双引号都行）
name = "Tang Ian"  


# --- 任务 3：浮点数 float ---
# 把 height 写成你的身高，单位米，要带小数点，例如 1.75
height = 1.75  


# --- 任务 4：布尔 bool ---
# 把 is_student 写成 True 或 False（首字母大写，不要引号）
is_student = True 


# --- 任务 5：算一下 ---
# 让 age_next 等于 age 加 1
# 提示：直接写 age + 1，Python 会自己算
age_next = age+1


# --- 任务 6：拼一句话 ---
# 让 greeting 等于下面这句话（用 f-string 拼，别自己手打数字）：
#   Hello, Tang Ian! You are 18 next year.
# 提示：f"Hello, {name}! You are {age_next} next year."
# 注意：18 那个位置要用 {age_next}，不能手打，否则算错分
greeting = f"Hello, {name}! You are {age_next} next year."


# ============================================
# 下面这行不用改，它会把你拼的句子打出来
print(greeting)
