# ============================================
# 第 1 课 自动检查器 v2
# 跑法：python3 ~/dev/hello/check01.py
# v2 改进：除了看结果对不对，还检查你有没有真的用变量
#          （写死数字 = 不算过，因为你没学会"改一处，处处变"）
# ============================================
import ast
import io
import os
import sys
import importlib.util

HERE = os.path.dirname(os.path.abspath(__file__))
LESSON = os.path.join(HERE, "lesson01.py")


def load_lesson():
    spec = importlib.util.spec_from_file_location("lesson01", LESSON)
    mod = importlib.util.module_from_spec(spec)
    buf = io.StringIO()
    old = sys.stdout
    sys.stdout = buf
    try:
        spec.loader.exec_module(mod)
    finally:
        sys.stdout = old
    return mod


def parse_source():
    """把源码解析成语法树，用来检查'写法'而不只是'结果'"""
    with open(LESSON, encoding="utf-8") as f:
        src = f.read()
    tree = ast.parse(src)
    assigns = {}
    for node in ast.walk(tree):
        if isinstance(node, ast.Assign):
            for t in node.targets:
                if isinstance(t, ast.Name):
                    assigns[t.id] = node.value
    return assigns


def names_used(node):
    """这个表达式里用到了哪些变量名"""
    return {n.id for n in ast.walk(node) if isinstance(n, ast.Name)}


def fstring_vars(node):
    """f-string 里用花括号插入了哪些变量名"""
    if not isinstance(node, ast.JoinedStr):
        return set()
    out = set()
    for part in node.values:
        if isinstance(part, ast.FormattedValue) and isinstance(part.value, ast.Name):
            out.add(part.value.id)
    return out


def main():
    if not os.path.exists(LESSON):
        print(f"❌ 找不到 {LESSON}")
        return 1

    try:
        m = load_lesson()
        assigns = parse_source()
    except SyntaxError as e:
        print(f"❌ lesson01.py 有语法错误，第 {e.lineno} 行：{e.msg}")
        print("   常见原因：引号没配对、少了括号、中文引号被当成英文引号")
        return 1
    except Exception as e:
        print(f"❌ 运行 lesson01.py 时出错：{type(e).__name__}: {e}")
        print("   常见原因：某个变量名打错了，或者算了不存在的变量")
        return 1

    results = []

    def check(no, title, ok, hint, want, got):
        results.append(ok)
        print(f"{'✅' if ok else '❌'} 任务 {no}  {title}")
        if not ok:
            print(f"      现在是：{got!r}")
            print(f"      应该是：{want}")
            print(f"      提示：  {hint}")

    # 1 整数
    v = getattr(m, "age", None)
    check(1, "整数 age",
          isinstance(v, int) and not isinstance(v, bool) and 12 <= v <= 60,
          "写纯数字，不要引号、不要小数点。比如 age = 18",
          "0~60 之间的整数", v)

    # 2 字符串
    v = getattr(m, "name", None)
    check(2, "字符串 name",
          isinstance(v, str) and len(v.strip()) > 0,
          '必须带引号，比如 name = "Tang Ian"',
          "一段有内容的文字，带引号", v)

    # 3 浮点数
    v = getattr(m, "height", None)
    check(3, "浮点数 height",
          isinstance(v, float) and 1.0 < v < 2.5,
          "要带小数点，比如 height = 1.75。写成 175 或 2 都不算对",
          "1.0 ~ 2.5 之间、带小数点的数", v)

    # 4 布尔
    v = getattr(m, "is_student", None)
    check(4, "布尔 is_student",
          isinstance(v, bool) and v is True,
          '写 True（首字母大写、不加引号）。"True" 是字符串，不算对',
          "True", v)

    # 5 运算 —— 值要对，而且必须真的用了 age 这个变量
    v = getattr(m, "age_next", None)
    age_val = getattr(m, "age", None)
    expr = assigns.get("age_next")
    used_age = expr is not None and "age" in names_used(expr)
    value_ok = (isinstance(v, int) and not isinstance(v, bool)
                and isinstance(age_val, int) and v == age_val + 1)
    if value_ok and not used_age:
        check(5, "运算 age_next", False,
              "结果对了，但你写的是写死的数字。要写 age + 1 —— "
              "这样以后 age 改成 19，age_next 自己会变成 20",
              "右边写成 age + 1", ast.unparse(expr) if expr else "<空>")
    else:
        check(5, "运算 age_next", value_ok and used_age,
              "直接写 age + 1，让 Python 算，别手打数字",
              f"{age_val + 1 if isinstance(age_val, int) else '你的 age 加 1'}",
              v)

    # 6 f-string —— 句子要对，而且花括号里必须是变量
    v = getattr(m, "greeting", None)
    nm = getattr(m, "name", "")
    nx = getattr(m, "age_next", None)
    expr = assigns.get("greeting")
    used = fstring_vars(expr) if expr is not None else set()
    text_ok = (isinstance(v, str) and isinstance(nm, str) and isinstance(nx, int)
               and v.startswith("Hello, ") and nm in v
               and str(nx) in v and v.endswith("next year."))
    vars_ok = "name" in used and "age_next" in used
    if text_ok and not vars_ok:
        check(6, "f-string greeting", False,
              "句子对了，但花括号里插的不是变量。要写 "
              'f"Hello, {name}! You are {age_next} next year."',
              "花括号里用 {name} 和 {age_next}", ast.unparse(expr) if expr else "<空>")
    else:
        check(6, "f-string greeting", text_ok and vars_ok,
              'f"Hello, {name}! You are {age_next} next year." —— '
              "花括号里面写变量名，别写数字",
              "Hello, 你的名字! You are 年龄+1 next year.", v)

    score = sum(results)
    total = len(results)
    print()
    print("=" * 50)
    print(f"  得分：{score} / {total}")
    if score == total:
        print("  🎉 全对，而且全是用变量算的。这一课真过了。")
        print("  下一步：跟 Agent 说「第1课过了」，我提交作业 + 给第2课。")
    else:
        print(f"  还有 {total - score} 项没过。改完再跑一次就行。")
        print("  卡住超过 5 分钟就把 ❌ 那几行贴给 Agent。")
    print("=" * 50)
    return 0 if score == total else 1


if __name__ == "__main__":
    sys.exit(main())
