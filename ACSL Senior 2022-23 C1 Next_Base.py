"""
Input:
15 8 2
Output:
9
"""
# 使用"手搓一遍基本的n进制进位系统"实现的第一种算法
def next_base_num(base, num):
    base_list = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F", "G"] # 进制打表
    for i in range(-1, -len(num) - 1, -1):
        # if i == -len(num) - 1: 
            
        next_ch = base_list[base_list.index(num[i]) + 1] + (-i - 1) * "0" # 下一个期待数据为此数据在列表中的下一个数据， 先寻找索引再+1；从最右侧开始找
        print(f"trying to connect {num[:i]} with {next_ch}")
        
        if base_list.index(next_ch[0]) != base: # 加完之后这一位的索引(进制对应的数字)不等于进制，没有进位，return
            return num[:i] + next_ch
        print(f"进位出现. next_ch: {next_ch}") # 到这一步说明出现进位，需要继续处理
    return "1" + len(num) * "0" # 到这一步说明全部处理了一遍而且全部进位，直接返回一个大整数

next_num, base, start = input().split()
next_num, base = int(next_num), int(base)

ans_dict = {}
based_num = str(start)
for i in range(next_num):
    # 首先针对当前的进制下数字进行处理，统计当前数字中每个字符出现的数字
    for character in based_num:
        print(f"Now checking {character} in {based_num}")
        if ans_dict.get(character) != None: ans_dict[character] += 1 # 使用get()内置函数，查找是否存在该字符，有说明存在统计数据，自动+1
        else: ans_dict[character] = 1 # 不存在此字符，开始统计，设为1
    print(f"The ans_dict now is like: {ans_dict}")

    # 接下来开始进行下一个base进制数的生成
    based_num = next_base_num(base, based_num)
    print(f"The next one is going to be {based_num}")
ans_list = max(ans_dict.values())
print(ans_list)


"""
# Alternative Ans(使用进制转换来达成统计目标)

def b10_to_base(num, base):
    base_list = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"] # 进制打表
    remainder = 0
    strout = "" # 使用余数合成str字符串
    while num != 0:
        remainder = num % base
        strout = str(base_list[remainder]) + strout # 取余数然后根据数值下标对应字符合成
        num //= base # 把除数除一遍
    return strout

next_num, base, start = input().split()
next_num, base = int(next_num), int(base)

num_in_base10 = int(start, base) # 这里使用的是int(number, base)来把base进制数转为10进制
ans_dict = {}
for i in range(next_num):
    # 先生成出base10的数字在base进制下的数字
    based_num = b10_to_base(num_in_base10, base)
    print(f"The next one is going to be {based_num}")

    # 针对当前的进制下数字进行处理，统计当前数字中每个字符出现的数字
    for character in based_num:
        print(f"Now checking {character} in {based_num}")
        if ans_dict.get(character) != None: ans_dict[character] += 1 # 使用get()内置函数，查找是否存在该字符，有说明存在统计数据，自动+1
        else: ans_dict[character] = 1 # 不存在此字符，开始统计，设为1
    print(f"The ans_dict now is like: {ans_dict}")

    # 处理完毕，base10数字+1
    num_in_base10 += 1

ans_list = max(ans_dict.values())
print(ans_list)
"""