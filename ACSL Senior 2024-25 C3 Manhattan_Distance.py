"""
Input:
5 17 2
Output:
6

**quick notes
正弦波三角形模式中，数字按照从左至右、从右至左、再从左至右的顺序依次书写，行宽交替递减或递增。
行宽逐渐缩小，直至某一行仅剩一个数字；随后行宽逐渐扩大，直至恢复到初始宽度；之后再次缩小，如此循环往复。
下图展示了一个宽度为 5的正弦波三角形模式的前几行:

 1  2  3  4  5
 9  8  7  6
10 11 12
14 13
15
17 16
18 19 20
24 23 22 21

25 26 27 28 29
33 32 31 30
34 35 36
38 37
39
41 40
42 43 44
48 47 46 45

49 50 51 52 53
....
- 没啥好说的, 第一行的长度等同于宽度, 慢慢-1递减到1之后再一路加到宽度上限.
- 值得注意的一点是它的顺序, 第一行是正的, 第二行倒的, 然后正倒循环; 理论上每个我定的循环内都是正的开头, 不用额外计算

在正弦波三角形中，两个数字 M 和 N 之间的曼哈顿距离是指这两个数字在水平和垂直方向上的距离之和。
题目会给出一个正弦波三角形模式的宽度以及该模式中的两个数字M 和 N。
你的程序需要计算数字 M 和 N 之间的曼哈顿距离。
- 肯定不可能硬列, 明确有数据能够飙到100甚至1000的, 要拿巧劲
- 我可以设n n-1 n-2 …… 2 1 2 3 …… n-2 n-1为一个循环, 把里面一共多少个数设成一次循环, 然后除一下看一共多少次循环之后到了目标数, 再进行下一步
- (这本质上有点像是映射吧? 把很后面的映射到前面)
"""
def index_coor_calc(width, num):
    starting_distance = width ** 2 - 1
    num_start = 1 + starting_distance * ((num - 1) // starting_distance)
    print(f"Starting d {starting_distance}, and {num} is in the cycle with start {num_start}")
    # print((num - 1) // starting_distance)

    row_is_reversed = False # 这是个判断当前行的数字是否反过来数的指示器
    for i in range(2 * width - 2): # 接下来一个一个往前推过去来算坐标
        if width - i > 0: # 这是个简单的数这一行有几个元素的计数器
            length_of_row = width - i
        else:
            length_of_row = i - width + 2
        # print(length_of_row, row_is_reversed)

        if num_start + length_of_row > num: # 加完之后是下一行的开头, 如果大了说明num就在这一行
            print(f"{num} is in *index* row {i} in cycle with width {length_of_row} and starts with {num_start}, is reverse = {row_is_reversed}")
            
            # 把num的座标进行计算
            if row_is_reversed == False: # 正的！这个是正向数的！
                # 这里面num - num_start算的是num和这一行首位数的差值, 恰好是这一行中num的index
                x_index = num - num_start
            else: # 这个才是反的
                # 因为会反过来, 所以是这一行的最大index减去num的index来达到反转index的效果
                x_index = length_of_row - 1 - (num - num_start)
            # y要把当前循环累积的列数进行叠加, 叠加算法是: 本循环之前的累计循环数量 * 每个循环的行数 + 这个循环里面经过的行数
            y_index = ((num - 1) // starting_distance) * (2 * width - 2) + i

            print(f"{num} is in index position ({x_index}, {y_index})")
            return x_index, y_index

        else:
            num_start += length_of_row

        row_is_reversed = not row_is_reversed # 单次循环判断完会进行反转
    return -1, -1

width, m, n = map(int, input().split())
# 由于m和n可能差了很多导致不在一趟"循环"内, 所以单独计算两者坐标.
# 先计算m那边循环的起始点
"""starting_distance = width ** 2 - 1
m_start = 1 + starting_distance * ((m - 1) // starting_distance)
print(f"Starting d {starting_distance}, and {m} is in the cycle with start {m_start}")
# print((m - 1) // starting_distance)

row_is_reversed = False # 这是个判断当前行的数字是否反过来数的指示器
for i in range(2 * width - 2): # 接下来一个一个往前推过去来算坐标
    if width - i > 0: # 这是个简单的数这一行有几个元素的计数器
        length_of_row = width - i
    else:
        length_of_row = i - width + 2
    # print(length_of_row, row_is_reversed)

    if m_start + length_of_row > m: # 加完之后是下一行的开头, 如果大了说明m就在这一行
        print(f"{m} is in *index* row {i} in cycle with width {length_of_row} and starts with {m_start}, is reverse = {row_is_reversed}")
        
        # 把m的座标进行计算
        if row_is_reversed == False: # 正的！这个是正向数的！
            # 这里面m - m_start算的是m和这一行首位数的差值, 恰好是这一行中m的index
            x_index = m - m_start
        else: # 这个才是反的
            # 因为会反过来, 所以是这一行的最大index减去m的index来达到反转index的效果
            x_index = length_of_row - 1 - (m - m_start)
        # y要把当前循环累积的列数进行叠加, 叠加算法是: 本循环之前的累计循环数量 * 每个循环的行数 + 这个循环里面经过的行数
        y_index = ((m - 1) // starting_distance) * (2 * width - 2) + i

        print(f"{m} is in index position ({x_index}, {y_index})")
        break

    else:
        m_start += length_of_row

    row_is_reversed = not row_is_reversed # 单次循环判断完会进行反转
"""
m_x, m_y = index_coor_calc(width, m)
n_x, n_y = index_coor_calc(width, n)
print(abs(m_x - n_x) + abs(m_y - n_y))

