"""
Input:
RWGBG
RCMGB
BYYGR
MRGBW
YYYYY
Output:
01:35:15
03:20:40
08:30:05
02:10:20
01:00:00
"""
for _ in range(5):
    display = input()
    hour, min, sec = 0, 0, 0 # 时分秒分开处理
    f0 = 0
    fib = 1 # 这里用俩数简单模拟一下斐波那契，虽然只需要取数列的前5项
    for i in range(5):
        # 没得简化，7种字符有6种都得单独列出来
        if display[i] == "R":
            # 对应小时
            hour += fib
            print(f"Hour += {fib} = {hour}")

        elif display[i] == "G":
            # 对应分钟
            min += fib * 5
            print(f"Minute += 5 * {fib} = {min}")

        elif display[i] == "B":
            # 对应秒
            sec += fib * 5
            print(f"Second += 5 * {fib} = {sec}")

        elif display[i] == "Y":
            # 同时对应小时和分钟
            hour += fib
            min += fib * 5
            print(f"Hour += {fib} = {hour}")
            print(f"Minute += 5 * {fib} = {min}")
        
        elif display[i] == "M":
            # 同时对应小时和秒
            hour += fib
            sec += fib * 5
            print(f"Hour += {fib} = {hour}")
            print(f"Second += 5 * {fib} = {sec}")

        elif display[i] == "C":
            # 同时对应分钟和秒
            min += fib * 5
            sec += fib * 5
            print(f"Minute += 5 * {fib} = {min}")
            print(f"Second += 5 * {fib} = {sec}")

        # 白色(W)不用写，题目要求忽略，我这里多加一个当作调试数据生成
        elif display[i] == "W":
            print("White doesn't count")
        # 接下来继续生成下一个斐波那契
        f0, fib = fib, f0 + fib
    print(f"The time now looks like: {hour}:{min}:{sec}")

    # 此时时分秒应该都生成好对应数据了，开始进行进位
    min += sec // 60
    sec %= 60
    hour += min // 60
    min %= 60
    hour %= 12

    # 输出，还是要补位
    print(f"{str(hour).zfill(2)}:{str(min).zfill(2)}:{str(sec).zfill(2)}")

