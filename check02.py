# ============================================
# 第 2 课 自动检查器
# 跑法：python3 ~/dev/hello/check02.py
# 判分原则：结果对 + 你真的用了列表和 for 循环（写死不认）
# ============================================
import ast
import io
import os
import sys
import importlib.util

HERE = os.path.dirname(os.path.abspath(__file__))
LESSON = os.path.join(HERE, "lesson02.py")


def load_lesson():
    spec = importlib.util.spec_from_file_location("lesson02", LESSON)
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
    with open(LESSON, encoding="utf-8") as f:
        src = f.read()
    tree = ast.parse(src)
    assigns = {}
    for node in ast.walk(tree):
        if isinstance(node, ast.Assign):
            for t in node.targets:
                if isinstance(t, ast.Name):
                    assigns[t.id] = node.value
    return tree, assigns


def for_loops_with(tree, need_print=False, need_total=False):
    """找出符合条件的 for 循环"""
    hits = 0
    for node in ast.walk(tree):
        if not isinstance(node, ast.For):
            continue
        body_ok = True
        if need_print:
            has_print = any(
                isinstance(s, ast.Expr)
                and isinstance(s.value, ast.Call)
                and isinstance(s.value.func, ast.Name)
                and s.value.func.id == "print"
                for s in node.body
            )
            body_ok = body_ok and has_print
        if need_total:
            has_add = False
            for s in node.body:
                if isinstance(s, ast.AugAssign) and isinstance(s.target, ast.Name) \
                        and s.target.id == "total":
                    has_add = True
                if isinstance(s, ast.Assign) and any(
                        isinstance(t, ast.Name) and t.id == "total" for t in s.targets):
                    has_add = True
            body_ok = body_ok and has_add
        if body_ok:
            hits += 1
    return hits


def main():
    if not os.path.exists(LESSON):
        print(f"❌ 找不到 {LESSON}")
        return 1

    try:
        tree, assigns = parse_source()
    except SyntaxError as e:
        print(f"❌ lesson02.py 有语法错误，第 {e.lineno} 行：{e.msg}")
        print("   常见原因：冒号漏了、缩进不一致、引号或方括号没配对")
        return 1

    try:
        m = load_lesson()
    except Exception as e:
        print(f"❌ 运行 lesson02.py 时出错：{type(e).__name__}: {e}")
        print("   常见原因：对 None 用了 .append()、变量名拼错、或者 for 循环缩进错")
        print("   先把报错修掉，再判分。")
        return 1

    results = []

    def check(no, title, ok, hint, want, got):
        results.append(ok)
        print(f"{'✅' if ok else '❌'} 任务 {no}  {title}")
        if not ok:
            print(f"      现在是：{got}")
            print(f"      应该是：{want}")
            print(f"      提示：  {hint}")

    nums = getattr(m, "nums", None)

    # --- 任务 1：列表字面量里必须是 4 个整数 ---
    expr = assigns.get("nums")
    lit_ok = (isinstance(expr, ast.List)
              and len(expr.elts) == 4
              and all(isinstance(e, ast.Constant) and isinstance(e.value, int)
                      and not isinstance(e.value, bool) for e in expr.elts))
    check(1, "造一个 4 个整数的列表",
          lit_ok and isinstance(nums, list),
          "写 nums = [3, 7, 1, 9] 这种。方括号里 4 个数，用逗号隔开",
          "方括号里 4 个整数",
          f"{nums!r}" if isinstance(nums, list) else repr(nums))

    # --- 任务 2：取第一个元素 ---
    first = getattr(m, "first", None)
    sub_ok = isinstance(assigns.get("first"), ast.Subscript)
    expect_first = nums[0] if isinstance(nums, list) and nums else None
    check(2, "取第一个元素",
          sub_ok and first == expect_first and expect_first is not None,
          "第一个元素要写 nums[0]，方括号里写 0，不是 1",
          f"nums[0] = {expect_first}", repr(first))

    # --- 任务 3：append ---
    append_ok = any(
        isinstance(n, ast.Call)
        and isinstance(n.func, ast.Attribute)
        and n.func.attr == "append"
        for n in ast.walk(tree)
    )
    appended = (isinstance(nums, list) and len(nums) == 5 and nums[-1] == 100)
    check(3, "往末尾加 100",
          append_ok and appended,
          "写一行 nums.append(100)，前面不要加 nums = ",
          "列表变成 5 个元素，最后一个是 100",
          f"{nums!r}" if isinstance(nums, list) else repr(nums))

    # --- 任务 4：len ---
    count = getattr(m, "count", None)
    check(4, "数一数有几个",
          count == (len(nums) if isinstance(nums, list) else None) and count is not None,
          "写 count = len(nums)，len 会自动数，别自己写数字",
          f"{len(nums) if isinstance(nums, list) else '?'}", repr(count))

    # --- 任务 5：for + print ---
    loops_print = for_loops_with(tree, need_print=True)
    check(5, "用 for 循环逐个打印",
          loops_print >= 1,
          "写 for n in nums: 然后缩进 print(n)。两行都要有",
          "一个里面含 print(...) 的 for 循环",
          f"找到 {loops_print} 个符合的 for 循环")

    # --- 任务 6：for + 累加 ---
    total = getattr(m, "total", None)
    expect_total = sum(nums) if isinstance(nums, list) else None
    loops_sum = for_loops_with(tree, need_total=True)
    empty_list = isinstance(nums, list) and len(nums) == 0
    ask = ("先把任务 1 的列表填好，再回来算总和"
           if empty_list else f"{expect_total}")
    check(6, "用 for 循环求和",
          loops_sum >= 1 and total == expect_total and expect_total is not None,
          "循环里写 total += n（等于 total = total + n），最后 total 应该是所有数的和",
          ask, repr(total))

    score = sum(results)
    total_q = len(results)
    print()
    print("=" * 50)
    print(f"  得分：{score} / {total_q}")
    if score == total_q:
        print("  🎉 全对，而且 for 循环是真写的。第 2 课过了。")
        print("  下一步：跟 Agent 说「第2课过了」，我提交 + 给第 3 课。")
    else:
        print(f"  还有 {total_q - score} 项没过。改完再跑一次就行。")
        print("  报错看不懂就把红字整段贴给 Agent。")
    print("=" * 50)
    return 0 if score == total_q else 1


if __name__ == "__main__":
    sys.exit(main())
