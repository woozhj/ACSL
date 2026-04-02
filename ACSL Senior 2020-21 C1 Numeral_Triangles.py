"""
Input:
A 9 5
ABC F 4
BAD 50 10
FED ABC 25
184 231 35
Output:
5
C
A
F
5
"""
def ten_to_hex(num):
    remainder = 0
    hexout = ""
    hexlist = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"] # 进制打表

    while num > 0:
        remainder = num % 16 # 因为只需要hex转dec, 所以对16取余就没了
        hexout = hexlist[remainder] + hexout # 取余之后根据进制表下标对应数值接在前面
        num //= 16

    return hexout

def single_trans(num):
    # remainder = 0
    digitout = 0
    # hexlist = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"] # 我还是那么爱打表

    # 这个因为是为了向单个字符推进的，所以会把每个输入的dec数在转hex过程中就把hex对应的dec数据加上去，最终返回的是一个浓缩过后的十进制数
    # 可以理解为hex对应的dec输进来，然后在转的时候把每一位的hex的dec值加起来，最后输出的是hex每一位总和的dec值
    while num > 0:
        digitout += num % 16 # 余数就是每一位hex的dec值，直接加进来就可以了
        num //= 16

    print(f"The sum of every digit in dec is {digitout}")
    return digitout


for _ in range(5):
    start, delta, rows = input().split()
    rows = int(rows)
    delta = int(delta, 16)
    previous_num = int(start, 16) # 使用int(num, base)快速转为十进制
    previous_num += int(delta * rows * (rows - 1) / 2) # 这里使用求和公式n(n-1)/2求出经过了多少项，再乘以公差delta直接得出第rows行的第一个数据值
    print(f"The first hex value in {rows}th row is {ten_to_hex(previous_num)}, which in dec is {previous_num}")

    sum = 0
    for i in range(rows):
        print(f"Dealing with {ten_to_hex(previous_num)}")
        # 首先对当前previous_num进行处理，这里使用特殊函数处理
        sum += single_trans(previous_num)
        # sum每次都会增加"当前处理数转为hex之后每位相加得到的dec总和"
        previous_num += delta

    # 得到一个初步的总和，接下来拿while把它削减到只剩一位，还是用特殊函数
    # 正常的判断条件是判断数据的hex是否大于一位，由于每次都要调用ten_to_hex()函数导致时间复杂度增加，所以采用数据dec是否大于等于16作为判断条件
    while sum >= 16:
        sum = single_trans(sum)

    # 最终输出一定是0-F的hex，给他转回去(本质上还是可以打表，可能还快点)
    print(ten_to_hex(sum))
