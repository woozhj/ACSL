"""
Input: (一行一行输入输出, 不是全部输入全部输出)
This is an Example of Sorting an interesting string
HackerRank.com was used for the ACSL Finals this year.
The digits of PI are 3.141592653.
She sells seashells by the seashore.
Programming languages include Java, Python, C++, Visual BASIC, Ruby, and Scratch.

Output:
6in,4ts,3aegr,2o,1ESTfhlmpx
5a,4se,3r,2tonkihc,1ACFHLRSdflmuwy
2135ei,1tsrohgfdaTPI9642
7es,4lh,2a,1ytrobS
8a,5n,4gu,3rlic,2CPSdehmosty,1vbVRJIBA

**quick notes
首先只保留字母和数字字符 (即 0-9, A-Z, a-z)，将剩下的字母进行排序，
然后重新排列包含重复字母的字符块，使得包含字母数量多的字符块排在前面。
- 这个题实验一下很快知道是个剔除+排序的process, 而且还是拿ASCII来排序的 (0-9A-Za-z顺序) 剔除容易, 打个表(没错打表真的太方便了)

如果字符块内包含字母的种类数目相同，那么第一个字符块按照递增顺序排列，第二个字符块按照递减顺序排列，第三个按照递增顺序排列，依此类推。
- 这里我把list.sort和list.reverse用上就可以了, 问题不大

最后，以简写形式打印输出这个字符串：先打印输出每个字符块的大小，然后打印输出每个字符块包含的字符，用逗号将每个大小不同的字符块分隔开。


"""
origin_str = input()
req_str_table = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz" # 极速打个表先
# times_appeared = [] # 我想着用列表打一个长一点的, 按照元素出现次数顺序列出表格(大概意思是[[1, ["a"]], [2, ["b"]]]这样? 不过会很麻烦.)
count_table = {} # 初版先拿字典速敲一个

for ch in range(len(origin_str)): # 这一步循环只用作统计
    if origin_str[ch] in req_str_table:
        if origin_str[ch] not in count_table:
            count_table[origin_str[ch]] = 1
        else:
            count_table[origin_str[ch]] += 1

# print(count_table)
count_table = sorted(count_table.items(), key = lambda dic: (dic[1], dic[0]), reverse = True) # 更新了字典顺序(逆序)
print(count_table)

out_dict = {}
last_times = -1 # 初始化流程, 记录上一个"出现次数"
char_list = []
for sets in count_table: # 用items()遍历字典
    if last_times != sets[1]: # 如果不一样就建立新的key-value, 然后更新last_times
        
        if last_times != -1: # 不是第一次开始循环, 需要进行列表更新
            out_dict[last_times] = char_list
            char_list = []
        
        last_times = sets[1]
    
    char_list.append(sets[0]) # 不断加进"出现了那么多次"的字符, 直到次数改变的时候把字符表打进输出用字典.

out_dict[last_times] = char_list # 循环退出之后还要更新不然会少一组
print(out_dict)

output_str = ""
is_reversed = False
# 现在out_dict能看到次数和出现对应次数的字符, 可以进行输出
for times, character_list in out_dict.items():
    char_block = str(times)
    block_list = sorted(character_list, reverse = is_reversed)

    for i in block_list:
        char_block += i
    
    output_str += char_block + ","

    is_reversed = not is_reversed # 更新状态

print(output_str[:-1])
