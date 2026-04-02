"""
IN - OUT
FIB1123
BOR

NPR9876
DE

DEF5470
BHIO

CAR2552
OPR

BOB1236
OPRS

HAP0037
R

*Quick Notes*
输入格式: 三个字母+四个数字 e.g.ABC0347 这样

1. 所有字母在字母表前半部分:"B"(Beginning)
都在后半部分就是"E"(Ending)
- 这个直接打表会好一点, 但是边界得看题目需求. 都是大写字母.

2. *所有*字母按字母表顺序*连续*排列/*所有*数字按数值*连续*排列:(两个只能选一个, 也就是说都满足的话不能输出)
递增是"I"(Increasing), 递减是"D"(Decreasing)
- 这个我需不需要打表? 可能得看

3. 字母可构成16进制数输出"H"
- 这个容易, 判断一下是不是都小于等于F(ASCII)就好了

4. 数字可构成最前面没0的八进制数输出"O"
- 也可以用小于8(ASCII)来判断, 多一步最前面有没有0的判断即可

5. 字母或者数字构成回文(这个好像没说不能同时满足, 拿or好了)输出"P"
- 这个可以用[::-1]字符串和原串比较来判断, 一定得把数字和字符分开来了

6. 存在重复字母/数字输出"R"
- 这个可以直接用某一个count整个串 == 2输出, 我回忆一下count咋做先
- 就是直接string.count("character") == 2好了

7. 任意三个数字和等于剩下那个输出"S"
- 唯一一个看着有点难度的, 思考一下

- 按顺序检测就行了, 但是输出需要排序, 都没有输出"NONE"
- 可用"".join(sorted(final_output))
"""
plate = input()
letters, numbers = plate[:3], plate[3:]
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
digits = "0123456789"
final_output = ""

# 第一步先查字母表, 前13个[:13]出"B", 后13个[13:]出"E"
# print(f"Start checking 1")
begin_count, end_count = 0, 0
for ch in letters:
    if ch in alphabet[:13]: # 前面13个
        begin_count += 1
    elif ch in alphabet[13:]:# 后面13个
        end_count += 1

if begin_count == 3:
    final_output += "B"
elif end_count == 3:
    final_output += "E"

# print(f"Done checking 1, final output {final_output}")

# 第二步查连续排列, 这里我拿个初始False的状态, 字母连续和数字连续都会反转他, 两次反转还是False没啥问题
continuous = False
if letters in alphabet or letters[::-1] in alphabet: # 字母是否连续
    continuous = not continuous
if numbers in digits or numbers[::-1] in digits: # 数字是否连续
    continuous = not continuous

# print(f"Start checking 2, the continuous mark is now {continuous}")
if continuous:
    if letters in alphabet or numbers in digits: # 这个就是正向的
        final_output += "I"
    elif letters[::-1] in alphabet or numbers[::-1] in digits: # 这个是反向的
        final_output += "D"

# print(f"Done checking 2, final output {final_output}")

# 第三步查16进制, 对比ASCII <= "F"即可
# print(f"Start checking 3")
is_hex = True
for ch in letters: # 拿标记查, 如果超范围就砍掉循环, 稍微加快一点速度
    if ch > "F":
        is_hex = False
        break

if is_hex:
    final_output += "H"

# print(f"Done checking 3, final output {final_output}")

# 第四步查8进制, 首位是否为0直接查[0]就得了, 其他的查ASCII
# print(f"Start checking 4")
is_oct = True
for ch in numbers:
    if ch >= "8": # 也是一样拿标记查
        is_oct = False
        break

if is_oct and numbers[0] != "0": # 同时保证首位不能是0
    final_output += "O"

# print(f"Done checking 4, final output {final_output}")

# 第五步查回文, 拿[::-1]和自己比一下就好了; 他还特地说是字符串, 不需要把数字转换成int挺好的
# print(f"Start checking 5")
if numbers[::-1] == numbers or letters[::-1] == letters: # 我和反向的我一样那就算回文了
    final_output += "P"

# print(f"Done checking 5, final output {final_output}")

# 第六步查重复的字符, 图个方便我拿原始串查好了
# print(f"Start checking 6")
for ch in plate:
    if plate.count(ch) == 2: # 出现了2次那就说明有重复的, 题目还说"不一定相邻"这么好心么
        final_output += "R"
        break

# print(f"Done checking 6, final output {final_output}")

# 第七步有点难度, 任意三个数字和等于剩下那个的话输出"S", 本质上我排序一下数字之后前三个小的和等于最后那个大的不就得了?
# print(f"Start checking 7")
numbers = sorted(numbers)
if int(numbers[0]) + int(numbers[1]) + int(numbers[2]) == int(numbers[3]):
    final_output += "S"

# print(f"Done checking 7, final output {final_output}")
if len(final_output) > 0:
    print("".join(sorted(final_output)))

else:
    print("NONE")
