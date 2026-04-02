"""
Input:
13256709 3
3587612098 1
265472 5
3126854901231 4
25768437216701562 7
Output:
789
49
46547
12798
15413544
"""
for _ in range(5):
    numstr, div = input().split()
    div = int(div)
    while len(numstr) % div != 0:
        numstr += "0" # 预先处理输入的数字字符串，保证其能够被分成长度都为div的字符串，也就是在最后面补0

    sum = 0
    for i in range(0, len(numstr), div): # 非常简单的一个隔位取字符，每个需求的数就直接是取到的字符往后再取div位而已
        print(f"{numstr[i:i + div]} is added to sum.")
        sum += int(numstr[i:i + div])
        print(f"The sum now looks like {sum}")
    print(sum)
