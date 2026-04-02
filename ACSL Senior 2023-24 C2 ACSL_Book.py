"""
Input:
ACSL, or the American Computer Science League, is an international computer science competition among more than 300 schools.  Originally founded in 1978 as the Rhode Island Computer Science League, it then became the New England Computer Science League.
American Computer Science League (ACSL) is fun!

Output:
1.1.1 1.5.3 1.5.7 1.10.5 1.10.9 1.12.6 1.16.3 1.13
.11_2.18.1 1.18.5 1.14.2 1.13.4 2.11.5 2.18.6 2.6.
3 2.9.8_2.19.1 2.10.2 2.1.3 2.11.2 1.16.4 2.14.3 2
.14.2_2.11.1 2.15.3 2.17.5 2.20.4 2.18.5 2.19.7_(1
.1.1 2.9.1 2.19.1 2.20.1)_1.13.9 1.18.7_2.2.1 2.2.
3 2.19.5!
(此处使用过美化数据, 实际数据为一行)

**quick notes
● Any keyboard character can be included in the text or the message and all alphabetic
characters are case sensitive

● A word in the text contains only alphanumeric characters and all words are separated by a
single space or any non-alphanumeric character(s)
一个"词"永远由非数字非字母类字符组成 e.g. 11/23/25含有3个词
***重点: 如何"局内分词", 例如多个非解码字符型字符 e.g. ,, ,,不可多次分词, 只能作为一个分词.
我想到的是切换形态式的检测器, 碰到解码字符时词位置指针+1, 之后转为检查非解码字符; 碰到非解码字符后恢复为解码字符查找

● All sentences in the text will end with a period, question mark, or exclamation point and
will be separated by exactly 2 spaces

● Only alphanumeric characters in the message will be encoded and all other characters
will remain as they are in the encoded message
只处理数字或字母类字符 e.g. (this is great!) 中括号和感叹号照常输出

● If a space occurs in the message, use an underscore ("_") for that character when
encoding it

###Important:

● For every character in the message to be encoded, find the location of the 1st occurrence
in the text of the 1st character in the message, the 2nd occurrence in the text of the 2nd
character in the message, the 3rd occurrence in the text of the 3rd character in the
message, etc.
限制了一波, 最好用index检查不然大概率索引跟不上. 不过由于只计算字符, 需要多加一个index变量

● We guarantee that each character in the message will occur at least once in the text
肯定有, 不用额外编写模块检测

● If there aren't that many occurrences of a character found in the text, divide the number
in half using integer division until that number of occurrences of that character is found
(e.g. if there is no 13th occurrence of a character, find the 6th, then the 3rd, then the 1st if
needed)

● Each encoded “s.w.c” within a word will be separated by a single space

ACSL, or the American Computer Science League, is an international computer science competition among more than 300 schools.  Originally founded in 1978 as the Rhode Island Computer Science League, it then became the New England Computer Science League.  With countrywide and worldwide participants, it became the American Computer Science League.  It has been in continuous existence since 1978.  Each yearly competition consists of four regular-season contests.  All students at each school may compete, but the team score is the sum of the best 3 or 5 top scores.  Each contest consists of 2 parts: a written section (called shorts) and a programming section.  Written topics tested include what does this program do, digital electronics, Boolean algebra, computer numbering systems, recursive functions, data structures (primarily dealing with heaps, binary search trees, stacks, and queues), Lisp programming, regular expressions and Finite State Automata, bit string flicking, graph theory, assembly language programming, and prefix/postfix/infix notation.
ACSL (American Computer Science League) is forty-six years old in '23!
1.1.1 1.5.1 2.10.1 2.20.1_(8.38.1 1.15.1 1.7.6 2.9.8 2.1.3 2.10.6 2.11.3 2.2.4_2.9.1 2.18.2 6.7.3 8.14.4 6.8.2 3.5.11 2.10.7 6.19.2_3.11.1 4.7.4 4.4.1 2.14.6 4.3.4 5.9.1 2.18.7_2.11.1 2.19.7 7.1.2 8.22.7 6.2.3 3.4.9)_7.14.9 7.11.6_8.49.5 7.4.1 8.21.2 6.17.4 8.44.8-8.11.11 8.11.9 8.50.5_6.6.3 4.6.1 8.22.3 8.34.4 8.20.10_8.14.2 8.45.1 7.12.3_8.32.9 8.29.2_'7.5.1 1.17.1!
1.1.1 1.5.1 2.10.1 2.20.1_(8.38.1 1.15.1 1.7.6 2.9.8 2.1.3 2.10.6 2.11.3 2.2.4_2.9.1 2.18.2 6.7.3 8.14.4 6.8.2 3.5.11 2.10.7 6.19.2_3.11.1 4.7.4 4.4.1 2.14.6 4.3.4 5.9.1 2.18.7_2.11.1 2.19.7 7.1.2 8.22.7 6.2.3 3.4.9)_7.14.9 7.11.6_8.49.5 7.4.1 8.21.2 6.17.4 8.44.8-8.11.11 8.11.9 8.50.5_6.6.3 4.6.1 8.22.3 8.34.4 8.20.10_8.14.2 8.45.1 7.12.3_8.32.9 8.29.2_'7.5.1 1.17.1!
"""

def index_validation(index, text, character):
    total_count = 0
    for sentences in text:
        total_count += sentences.count(character) # 先统计一下一共有多少个此字符
    # print(f"Counted a total of {total_count} character {character}")
    while index > total_count:
        index = int(index / 2) # 十分简单的直接向下取整, 直到index比字符总数小/等于总数
    return index

def encode(character, text, index): # 中央核心处理函数, 实现切换状态的字符, 单词和句子统计
    index = int(index)
    
    alphanum_list = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ" # 表格迁移
    n_th_sentence = 0
    n_th_word = 0
    n_th_character = 0
    
    ch_finding = True
    sep_finding = False # 交换状态的双状态检测变量
    
    for j in range(len(text)):
        n_th_sentence += 1 # 句子会自动切换, 不需要进行多状态处理
        n_th_word = 0 # 必须在每个句子扫完之后重置单词

        if character in str(text[j]): # 提速: 把句子转回str然后拿in快速检测句子内含不含有这个字符
            for i in range(len(text[j])):
                # 先进行状态检测和交换
                if text[j][i] in alphanum_list and ch_finding: # 状态: 寻找解码字符
                    n_th_word += 1
                    ch_finding, sep_finding = sep_finding, ch_finding
                
                elif text[j][i] not in alphanum_list and sep_finding: # 状态: 寻找分隔词语的非解码字符
                    n_th_character = 0 # 如果现在看到的字符为非解码字符, 则单词遍历结束, 重置字符值
                    ch_finding, sep_finding = sep_finding, ch_finding

                if text[j][i] in alphanum_list and sep_finding: # 此时在单个"单词"内, 可以进行"第n个字符"索引
                    n_th_character += 1

                # 然后才开始匹配字符
                if character == text[j][i]: # 拿当前字符匹配
                    index -= 1
                    if index == 0:
                        return n_th_sentence, n_th_word, n_th_character

text = list(map(list, input().split("  ")))
message = list(input())
encoded_msg = ""
alphanum_list = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ" # 懒, 还是打一个解码字符表得了, 判断直接用in来扣得了

# 循环遍历message检测每个字符
ch_index = 0
for i in range(len(message)):
    character = message[i]
    
    if character in alphanum_list:
        # 正常解码字符, 准备查找
        ch_index += 1 # 只有碰到解码类字符才会增加索引.注意索引只负责标记计算后需求的"第n个字符", 并不能直接用于索引,
        
        print(f"Finding {character} in text")
        index = index_validation(ch_index, text, character) # 这才是需要用到的索引, 经过有效化处理
        sentence, word, ch = encode(character, text, index)
        print(f"第{index}个 character {character} is in sentence no. {sentence}, word no. {word}, character no. {ch}.")
        encoded_character = str(sentence) + "." + str(word) + "." + str(ch) # 分别计算完所有的三个变量之后组合
        encoded_msg += encoded_character # 正常解码字符会以普通空格分隔
        
        # 接下来要额外增加一步判断需不需要增加空格分隔, 因为如果下一位不是解码字符的话是不需要增加空格补位的.
        # 由于句子一定以非解码字符结束, 可以放心使用字符串索引推后
        if message[i + 1] in alphanum_list:
            encoded_msg += " "
    
    elif character == " ":
        # 空格字符, 用下划线补位
        print(f"Get a space. Placing with _ .")
        encoded_msg += "_"
    
    else:
        # 非空格非解码字符, 直接补进去
        print(f"Other characters. Will be placed directly.")
        encoded_msg += character
    
    print(f"Dealed one character. encoded message now: {encoded_msg}")

print(encoded_msg)
