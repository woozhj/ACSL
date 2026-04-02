"""
Input:
31415926538
314159265
201617
123456789
1223334444
Output:
3 8 14 35 159
3 5 14 62 159
2 7 16
1 9 23 87 456
1 4 22 44 333
"""
def sectioning(secnum, tarnum):
    if int(secnum) < tarnum: return secnum, len(secnum) # 待截选数剩余部分已经无法比目标更大了，直接返回整个剩余的部分
    ret_num = str(secnum[0]) # 将返回的数初始化为待截选数第一位
    count = 1
    while int(ret_num) <= tarnum:
        ret_num += secnum[count] # 返回数一直往后接待截选数，直到比目标更大为止
        count += 1
    return ret_num, len(ret_num) # len(ret_num) 表示的是待截选数将要被截掉的长度
    """
    if len(secnum) >= seclen:
        return secnum[:seclen] # 如果待处理数的长度已经足够就可以用此方法截选
    return secnum # 到这里说明长度不足，直接返回整个数
    """

for _ in range(5):
    strnum = input()
    sec_length = 0

    ans_list = []
    dealing_num = strnum # 待处理数
    outnum = 0 # 输出数
    # incr_sec_len_count = 0 # 截选长度增加标记
    while len(dealing_num) > 0:

        dealing_num = str(int(dealing_num)) # 预处理待处理数，确保最前方多余的0不会影响后续输出
        print(f"The dealing num is now like {dealing_num}")
        sectioned_num, sec_length = sectioning(dealing_num, outnum) # 进行截选操作，得到准备截选的长度以及截出来的数
        sectioned_num, sec_length = int(sectioned_num), int(sec_length)
        print(f"Comparing {sectioned_num} with {outnum}")

        # 这里是处理输出部分的，遇到更大的被截选数则更新outnum，否则结束
        if sectioned_num > outnum:
            print(f"{sectioned_num} is greater than {outnum}, adding to ans_list.")
            ans_list.append(sectioned_num)
            print(f"ans_list looks like {ans_list}")
            outnum = sectioned_num # 碰到更大的数，更新outnum
        else:
            print(f"{sectioned_num} is smaller than {outnum}. END") # 新的截取数太小了，不输出，继续进行处理
            break

        dealing_num = dealing_num[sec_length:] # 把当前待处理数截掉已截选的部分
        print(f"sectioned. The dealing num is now like {dealing_num}")
        dealing_num = dealing_num[::-1] # 准备处理反向的待处理数
        # incr_sec_len_count += 1 # 截选长度增加标记增加

        # if incr_sec_len_count % 2 == 0:
            # sec_length += 1 # 标记为偶数说明正向反向都处理完了，截选长度+1

    for num in ans_list:
        print(num, end = " ")
    print()
