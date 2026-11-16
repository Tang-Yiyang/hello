# ============================================
# 布尔到底怎么用 —— 5 个真实场景
# 跑法：在 VS Code 里按 F5
# 目标：看完你能自己写 if
# ============================================

# --- 场景 1：直接写，把"事实"存起来 ---
# 这就是你任务 4 写的，布尔不用算，直接给
is_student = True
has_job = False
print("1) 是学生吗:", is_student)
print("   有工作吗:", has_job)


# --- 场景 2：比较，让 Python 自己算出布尔 ---
age = 18
can_vote = age >= 18          # 右边会算出一个 True/False，再存进左边
print("2) 能投票吗:", can_vote)


# --- 场景 3：真正干活的地方 —— if ---
# if 后面跟一个布尔，True 就执行冒号下面缩进的那几行，False 就跳过
if can_vote:
    print("3) → 你可以投票")
else:
    print("3) → 你还没到年龄")
# 注意：不用写 if can_vote == True:，直接写 if can_vote: 就行


# --- 场景 4：条件叠加 —— and / or / not ---
has_id_card = True
if can_vote and has_id_card:          # 两个都为 True 才进
    print("4) → 证件齐了，可以进投票站")

if has_job or is_student:             # 有一个为 True 就进
    print("4) → 你有身份（学生也算）")

if not has_job:                       # not 取反：False 变 True
    print("4) → 你目前没有工作，别急着交税")


# --- 场景 5：拿它当"开关" ---
# 这是最常用的写法：改一个 True/False，就能开关一整个功能
debug = False
if debug:
    print("5) 【调试信息】只在 debug=True 时才打印")
print("5) 程序继续往下跑")
