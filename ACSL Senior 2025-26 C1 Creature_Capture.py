"""
def calculate_loc(row_guess, col_guess, row_dist, col_dist):
    outlist = []
    # 我没想到啥技巧，硬举4个组合，顺带把边界判断给做了(不错老子就是屎山之王啊哈哈哈哈)
    if row_guess + row_dist <= 256:
        if col_guess + col_dist <= 256:
            outlist.append([row_guess + row_dist, col_guess + col_dist])
        
        if col_guess - col_dist >= 0:
            outlist.append([row_guess + row_dist, col_guess - col_dist])
    
    if row_guess - row_dist >= 0:
        if col_guess + col_dist <= 256:
            outlist.append([row_guess - row_dist, col_guess + col_dist])
        
        if col_guess - col_dist >= 0:
            outlist.append([row_guess - row_dist, col_guess - col_dist])
    return outlist

def loc_store(retlist, row, col, col_dist, row_dist):
    # 朴实无华的调换一下两个距离，再推一边(哥们我时间复杂度应该不会超吧)
    retlist += calculate_loc(row, col, row_dist, col_dist)
    retlist += calculate_loc(row, col, col_dist, row_dist)
    
    return retlist

def den_to_hex(num):
    hexlist = "0123456789ABCDEF" # 啊哈哈哈又是我, 打表之神
    outnum = ""
    while num > 0:
        outnum = hexlist[num // 16] + outnum
        num %= 16

    return outnum

loc_set1, loc_set2, loc_set3 = [], [], []

for _ in range(3):
    # 先快速处理输入，把猜测坐标和距离分离出来转10进制
    a, b = input().split()
    row = int(a[:2], 16)
    col = int(a[2:], 16)
    row_dist = int(b[:2], 16)
    col_dist = int(b[2:], 16)

    # print(f"guessing in {row}, {col}")
    # print(f"there's a distance in {row_dist}, {col_dist}!")
    # 数据转换为坐标集加进列表里
    if len(loc_set1) == 0:
        # 把两种距离互相调换扔进函数，出两套列表加进去，其余同理
        # print("add in 1")
        loc_set1 = loc_store(loc_set1, row, col, col_dist, row_dist)
    elif len(loc_set2) == 0:
        # print("add in 2")
        loc_set2 = loc_store(loc_set2, row, col, col_dist, row_dist)    
    elif len(loc_set3) == 0:
        # print("add in 3")
        loc_set3 = loc_store(loc_set3, row, col, col_dist, row_dist)
    # 由于不存在"猜测坐标经计算后没有任何点落在0-256范围"情况，使用len=0判断逻辑

# 循环完毕后所有可能坐标(10进制)计算完毕，寻找相同的共有坐标元素
# 这里用一下优化，找到长度最短的列表开始和其他两个表对比
len1, len2, len3 = len(loc_set1), len(loc_set2), len(loc_set3)
if len2 < len1 and len3 > len2: # 第二个坐标集元素最少
    loc_set1, loc_set2 = loc_set2, loc_set1

elif len3 < len1 and len2 > len3: # 第三个坐标集元素最少
    loc_set1, loc_set3 = loc_set3, loc_set1

# 此时把元素最少的挪到坐标集1，直接使用它来进行操作
print(f"for set1 {loc_set1}, set2 {loc_set2}, set3 {loc_set3}")
for hidden_loc in loc_set1:
    if hidden_loc in loc_set2 and hidden_loc in loc_set3:
        print(f"({den_to_hex(hidden_loc[0])},{den_to_hex(hidden_loc[1])})")
        break


"""


"""
输入数据 1
4D93 414D
A566 997A
F633 EAAD
输出数据 1
(0C,E0)
输入数据 2
093C A396
D675 2A5D
397E 7354
输出数据 2
(AC,D2)
输入数据 3
4C0D 3334
33BB 4C7A
EC8E 6D4D
输出数据 3
(7F,41)
输入数据 4
16FA AC24
57FD 6B27
63B4 5F22
输出数据 4
(C2,D6)
输入数据 5
B531 7760
C8FA 8A69
F543 B74E
输出数据 5
(3E,91)
输入数据 6
EF65 207B
6F4A 6096
43C8 8C18
输出数据 6
(CF,E0)
"""




def calculate_loc(row_guess, col_guess, row_dist, col_dist):
    outlist = []
    # 我没想到啥技巧，硬举4个组合，顺带把边界判断给做了(不错老子就是屎山之王啊哈哈哈哈)
    if row_guess + row_dist <= 256:
        if col_guess + col_dist <= 256:
            outlist.append([row_guess + row_dist, col_guess + col_dist])
        
        if col_guess - col_dist >= 0:
            outlist.append([row_guess + row_dist, col_guess - col_dist])
    
    if row_guess - row_dist >= 0:
        if col_guess + col_dist <= 256:
            outlist.append([row_guess - row_dist, col_guess + col_dist])
        
        if col_guess - col_dist >= 0:
            outlist.append([row_guess - row_dist, col_guess - col_dist])
    return outlist

def loc_store(retlist, row, col, col_dist, row_dist):
    # 朴实无华的调换一下两个距离，再推一边(哥们我时间复杂度应该不会超吧)
    retlist += calculate_loc(row, col, row_dist, col_dist)
    retlist += calculate_loc(row, col, col_dist, row_dist)
    
    return retlist

def den_to_hex(num):
    hexlist = "0123456789ABCDEF" # 啊哈哈哈又是我, 打表之神
    outnum = ""
    while num != 0:
        outnum = hexlist[num % 16] + outnum
        num //= 16

    return outnum

loc_set_current, loc_setfinal = [], []

for _ in range(3):
    # 先快速处理输入，把猜测坐标和距离分离出来转10进制
    a, b = input().split()
    row = int(a[:2], 16)
    col = int(a[2:], 16)
    row_dist = int(b[:2], 16)
    col_dist = int(b[2:], 16)

    # print(f"guessing in {row}, {col}")
    # print(f"there's a distance in {row_dist}, {col_dist}!")
    # 数据转换为坐标集加进列表里
    loc_set_current = []
    if _ == 0:
        # 第一组先初始化，把能加的数据都加进来
        loc_setfinal = loc_store(loc_setfinal, row, col, col_dist, row_dist)
    else: # 剩下两组进行筛选，只找共同有的加进当前的坐标集里 
        if [row + row_dist, col + col_dist] in loc_setfinal:
            loc_set_current.append([row + row_dist, col + col_dist])

        if [row + row_dist, col - col_dist] in loc_setfinal:
            loc_set_current.append([row + row_dist, col - col_dist])
        
        if [row - row_dist, col + col_dist] in loc_setfinal:
            loc_set_current.append([row - row_dist, col + col_dist])
        
        if [row - row_dist, col - col_dist] in loc_setfinal:
            loc_set_current.append([row - row_dist, col - col_dist])


        if [row + col_dist, col + row_dist] in loc_setfinal:
            loc_set_current.append([row + col_dist, col + row_dist])

        if [row + col_dist, col - row_dist] in loc_setfinal:
            loc_set_current.append([row + col_dist, col - row_dist])
        
        if [row - col_dist, col + row_dist] in loc_setfinal:
            loc_set_current.append([row - col_dist, col + row_dist])
        
        if [row - col_dist, col - row_dist] in loc_setfinal:
            loc_set_current.append([row - col_dist, col - row_dist])


        loc_setfinal = loc_set_current # 更新并缩小范围
    
    if len(loc_setfinal) == 1: # 范围足够小立刻输出
        print(f"({den_to_hex(loc_setfinal[0][0]).zfill(2)},{den_to_hex(loc_setfinal[0][1]).zfill(2)})")
        break
