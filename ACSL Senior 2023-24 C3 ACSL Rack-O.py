"""
Input:
9 70
40 35 30 56 32 58 44 17 45
31 37 10 28 21 62 7 64 16 12
Output:
7 10 21 31 32 37 44 62 64


8 100
6 13 47 62 32 70 76 12
3 67 80 10 39 44 2 43 90 85 21 63 4 52

解析：
9 个卡槽和 70 张卡牌的区间为:1-8、9-16、17-24、25-32、33-40、41-48、49-56、57-64、65-70。
如果抽到 23, 那么其理想卡槽为第 3 个卡槽, 因为卡槽 3 的理想数字组合是17-24。

**quick notes
我们将采用的启发式值指的是*递减*次数。
在此游戏中, 递减指的是牌架上某一张卡牌小于其前一卡槽中的卡牌(例如, 在 40、20、30、50、70中, 数字 40 后发生一次递减)。
如果牌架上有 0 次递减, 则表示整个牌架是按照升序排列, 此时游戏结束。
因此, 启发式值越低, 牌架上的卡牌排列情况越接近游戏目标。
如果以下策略中的某一种策略可行的话, 则执行这种策略。
这种策略要么能降低启发式值, 要么保持启发式值不变。
如果启发式值不变, 则选择策略A。否则, 放弃抽到的卡牌。
- 启发值依旧迷, 我还得数顺序, 目前暂定遍历一遍, 比i和i+1的大小
- 这里能看到一个简单的if判断: 算完启发值之后谁小选谁, 都一样选A
-- 碰到的错误: 判断的时候逻辑不怎么完美, 漏条件没跑通

**A**理想卡槽: 
为每个卡槽创建一个区间, 这个区间是一个理想的数字组合.
为了确定每个卡槽的区间大小, 可以使用公式。如果 n 是 s 的倍数, 则使用公式 n/s;
否则使用公式 int(n/s)+1。例如, 如果有 4 个卡槽和 25 张牌, 则每个区间的大小为 int(25/4)+1=7。
如果 n 不是 s 的倍数, 则最后一个卡槽的区间可能较小。
接下来, 确定每个卡槽中可能可以放置的数字。
例如, 对于卡槽 1-4, 每个卡槽可放置的数字范围分别为 1-7、8-14、15-21、22-25。
被抽到的卡牌可以被放在它理想的卡槽的前提是该卡槽中已经存在的卡牌不在其理想区间内。
例如, 如果抽到的卡牌20, 则只有当卡槽 3 中已经存在的卡牌不在 15 到 21 之间(包括 15 和 21)时, 才将其放在其卡槽 3 中。
- 一个分组的活动, 加上简单判断: 如果 当前牌能放的槽里 存在一个属于理想区间之外的值 那么 把这张牌放到那个地方.
-- 碰到的错误: 边界没收

**B**升序: 
从牌架前方开始, 找到第一组未按升序排列的3张卡牌。
在这一组卡牌中, 用抽到的卡牌替换其中某一张卡牌使得这3张卡牌按升序排列。
例如, 如果牌架上是 10、20、30、9、40, 那么第一组 3 个相邻但未按升序排列的卡牌数字就是20、30、9。
如果抽到的卡牌是33(或者任何一个比 30 大的数), 则将其放入第 4 个卡槽中。
如果抽到的卡牌是25, 则放弃使用这张卡牌。
如果还存在其他类似的组合, 则继续沿着牌架寻找下一组卡牌。
- 这个的判断有点迷, 主要是移动三个数字的框来搜索, 只要三个数字不是正序就会判定为非升序排列.
- 这三个数中需要找到"属于正序的最后一个"数, 然后看自己手上的比他大就换, 否则弃掉.
- 按理说我直接找到第一个比它前面要小的数字看能不能替换不就得了么?

一旦牌架上的卡牌按升序排列, 游戏结束, 不再抽牌。
当抽牌堆为空时, 游戏也会结束。
游戏结束时, 以一个数字字符串的形式输出整个牌架, 各数字之间用一个空格隔开。
"""
def step_down_count(slot):
    step_down = 0
    for i in range(len(slot) - 1):
        if slot[i] > slot[i + 1]:
            step_down += 1
            print(f"The value {slot[i]} is greater than value {slot[i + 1]}!")
    print(f"final count step-down {step_down}")
    return step_down

def A_ideal_slot(slot, curr_card, slot_range): # 返回执行A策略之后的新卡槽堆和对应递减值
    new_slot = slot[:]
    for i in range(len(slot_range)):
        if curr_card <= slot_range[i]: # 在这个边界内(包含下界不含上界)的判断
            print(f"This card {curr_card} is in range {slot_range[i - 1] + 1} to {slot_range[i]}")

            # 然后去查看现在的卡槽里放的牌是不是理想状态的
            if slot[i - 1] >= slot_range[i - 1] + 1 and slot[i - 1] <= slot_range[i]: # slot内的i-1正好是对应的牌.
                print(f"The card in slot {slot[i - 1]} is in the range, so don't place.")
            else:
                print(f"The card in slot {slot[i - 1]} is not in the range, placing.")
                """
                new_slot = slot[:i - 1]
                new_slot.append(curr_card)
                new_slot += slot[i:]
                """
                new_slot[i - 1] = curr_card
            break
    
    return new_slot, step_down_count(new_slot)

def B_asc_order(slot, curr_card): # 这个给的算法好奇怪, 三个"非升序"的数组里面通过替换来让他们仨变成升序. 我能大概知道有什么情况, 但是只能硬做他来着?
    new_slot = slot[:]
    can_place = False
    for i in range(len(slot) - 2):
        if not (slot[i + 2] > slot[i + 1] and slot[i + 1] > slot[i]):# 直接强行看是不是正序
            print(f"The group from {slot[i]} {slot[i + 1]} {slot[i + 2]} are not in order.")
            for j in range(3):
                new_slot = slot[:]
                print(f"When process, new slot {new_slot} and placing {curr_card} into pos {i + j}")
                """
                new_slot = slot[:i + j]
                new_slot.append(curr_card)
                new_slot += slot[i + j + 1:]
                """
                new_slot[i + j] = curr_card # 给每一个都替换一遍, 看什么时候它们仨是升序
                print(f"New slot now {new_slot}")
                if new_slot[i + 2] > new_slot[i + 1] and new_slot[i + 1] > new_slot[i]:
                    print(f"when {new_slot}, the three stuff are in order.")
                    can_place = True
                    break
        
        if can_place: # 有过替换行为了, 可以直接退出并返回
            break
    if not can_place: # 没办法放的话还是只能用slot来当作输出, 表示无放置
        new_slot = slot[:]
    return new_slot, step_down_count(new_slot)

slot_len, card_num = map(int, input().split())
slot = list(map(int, input().split()))
card = list(map(int, input().split()))

curr_step_down = step_down_count(slot)
# 本质上可以直接用向上舍入的方式定范围来着
if card_num % slot_len == 0:
    # 成倍数关系, 可以直接除
    range_size = card_num // slot_len
else: # 不是倍数就整除加一
    range_size = card_num // slot_len + 1

tmp = range_size
slot_range = [0]
while card_num > tmp: # 想了一下还是存一个范围表好了
    slot_range.append(tmp)
    tmp += range_size
slot_range.append(card_num) # 此时取用范围的方法: 数据的前一项+1到数据为一个范围.
print(slot_range)

while card and curr_step_down > 0:
    slot_A, step_down_A = A_ideal_slot(slot, card[0], slot_range)
    print(f"After plan A, new slot {slot_A} and new step_down {step_down_A}")
    slot_B, step_down_B = B_asc_order(slot, card[0])
    print(f"After plan B, new slot {slot_B} and new step_down {step_down_B}")

    # 先分别判断 A、B 是否"有效"
    # 有效 = 确实换了牌（slot 有变化）且启发值没有变差
    a_valid = (slot_A != slot) and (step_down_A <= curr_step_down)
    b_valid = (slot_B != slot) and (step_down_B <= curr_step_down)

    if a_valid and b_valid:
        # 两个都有效：启发值小的优先，相同则选 A
        if step_down_A <= step_down_B:
            slot = slot_A[:]
            curr_step_down = step_down_A
        else:
            slot = slot_B[:]
            curr_step_down = step_down_B
    elif a_valid:
        slot = slot_A[:]
        curr_step_down = step_down_A
    elif b_valid:
        slot = slot_B[:]
        curr_step_down = step_down_B
    # 否则两个都无效，跳过这张牌
    """
    if step_down_B <= curr_step_down or step_down_A <= curr_step_down: # 递减值两个中保持其不变或者更优出现就可以开始放了
        # 注意, 一定要是可以放才行！所以判定的时候多一句判断是否一样.
        if step_down_A <= step_down_B and slot_A != slot: # 相同或者A小的话就选A
            print(f"A is better!")
            slot = slot_A[:] # 一定要采用复制列表！
            curr_step_down = step_down_A
        elif step_down_B < step_down_A and slot_B != slot:
            print(f"B is better!")
            slot = slot_B[:] # 一定要采用复制列表！
            curr_step_down = step_down_B
    """
    print(f"After the process, the slot {slot} and card {card} ([0] will be poped)")
    card.pop(0) # 事实上放不放都会pop

out_l = []
for i in slot: # join()非要str, 只能循环一遍了.
    out_l.append(str(i))
fin_out = " ".join(out_l)
print(fin_out)
