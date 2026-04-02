"""
Input:
Roses are red.

Output:
4
**quick notes

1. 把接收到的玩意儿每一个都转成ASCII码并转为2进制, 补位到8位, 然后全部接在一起. 补位直接拿zfill(8)就可以实现
2. 拿得到的长二进制字符串, 从0开始来找每一个对应寻找数的二进制数, 直到找不到所需二进制数为止, 注意需要前后各找一个.
实例解析结果: 
0000110000011000010010010000000001000100
0000110000011000010010010000000001000100
3. 
"""
"""
def den_to_bin(num):
    num = int(num)
    outstr = ""
    while num > 0: # 经典的整除den转bin
        outstr = str(num % 2) + outstr
        num //= 2
    return outstr
"""
def Find_dealing(base_str, base):
    finding_base = 0
    if base == 2:
        finbase_str = f"{finding_base:b}" # 二进制字符串转化
    elif base == 8:
        finbase_str = f"{finding_base:o}" # 八进制字符串转化

    while base_str.find(finbase_str) > -1 or base_str.rfind(finbase_str) > -1: # 如果字符串内不存在的话就退出
        print(f"Finding {finbase_str} now.")
        # 从左侧开始找字符part
        left_index = base_str.find(finbase_str) # 从左边找到的第一个base进制寻找数的index

        if left_index > -1:
            print(f"L {finbase_str} is in index {left_index}")
            base_str = base_str[:left_index] + base_str[left_index + len(finbase_str):] # 左侧截选
            print(f"base_str now {base_str}")

        # 从右侧开始找字符part(必须两个part的index finding和删除挨在一起, 不然会干扰结果)
        right_index = base_str.rfind(finbase_str) # 从右边找到的第一个base进制寻找数的index

        if right_index > -1:
            print(f"R {finbase_str} is in index {right_index}")
            base_str = base_str[:right_index] + base_str[right_index + len(finbase_str):] # 右侧截选
            print(f"base_str now {base_str}")

        finding_base += 1 # 需要寻找的数字向后推进
        if base == 2:
            finbase_str = f"{finding_base:b}" # 二进制字符串转化
        elif base == 8:
            finbase_str = f"{finding_base:o}" # 八进制字符串转化
    
    return base_str, finding_base


s = input()

# ASCII转二进制部分
bin_str = ""

for ch in s:
    next_ord = (f"{ord(ch):08b}") # 每个单字符转换为ASCII对应的数字, 直接转成2进制
    # next_bin = den_to_bin(next_ord).zfill(8) # 转bin再补位
    bin_str += next_ord

print(f"After converting, bin_str now {bin_str}")

# 二进制处理部分
bin_str, finding = Find_dealing(bin_str, 2)
"""
finding_bin = 0
finbin_str = f"{finding_bin:b}" # 转字符串形式

while bin_str.find(finbin_str) > -1 or bin_str.rfind(finbin_str) > -1: # 如果字符串内不存在的话就退出
    print(f"Finding {finbin_str} now.")
    # 从左侧开始找字符part
    left_index = bin_str.find(finbin_str) # 从左边找到的第一个二进制寻找数的index

    if left_index > -1:
        print(f"L {finbin_str} is in index {left_index}")
        bin_str = bin_str[:left_index] + bin_str[left_index + len(finbin_str):] # 左侧截选
        print(f"bin_str now {bin_str}")

    # 从右侧开始找字符part(必须两个part的index finding和删除挨在一起, 不然会干扰结果)
    right_index = bin_str.rfind(finbin_str) # 从右边找到的第一个二进制寻找数的index

    if right_index > -1:
        print(f"R {finbin_str} is in index {right_index}")
        bin_str = bin_str[:right_index] + bin_str[right_index + len(finbin_str):] # 右侧截选
        print(f"bin_str now {bin_str}")

    finding_bin += 1 # 需要寻找的数字向后推进
    finbin_str = f"{finding_bin:b}"
"""
print(f"After bin_finding, bin_str now {bin_str}")

# 二转八重新处理部分
bin_val = int(bin_str, 2) # 被砍完之后二转十
oct_str = f"{bin_val:o}" # 十再转八

print(f"After converting, oct_str now {oct_str}")

# 八进制处理部分
oct_str, finding = Find_dealing(oct_str, 8)
print(f"After oct_finding, oct_str now {oct_str}")
print(finding - 1)
