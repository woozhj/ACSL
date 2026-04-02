"""
Input:
523.125, 6, 2
+523.125, 6, 1
-523.163, 6, 1
523.125, 4, 2
-523.12, 6, 1
Output:
523.13
+523.1
-523.2
#.##
-523.1

**quick notes
outlen < intlen + outdec + 1 or outdec > declen ———> cannot output, ###.###
then get outlen >= intlen + 1 + outdec.
1. numdec: 四舍五入, 保留outdec长度
2. numint: 在前面接上来
3. (if outlen > 1 + intlen + declen) "#" * 差值 + final_out 
"""
for _ in range(5):
    num, outlen, outdec = input().split(", ")
    outlen, outdec = int(outlen), int(outdec)
    numint, numdec = str(num).split(".") # 注意numint有概率出现符号位

    # 先进行初步判断，逻辑:如果输出小数位数(outdec)+输出整数位数(len(numint))+小数点(1)比输出总位数(outlen)大则长度过长 或者 要求输出小数位比拥有的小数位多
    # 则当作无法输出，统一用#处理
    if outdec + len(numint) + 1 > outlen or outdec > len(numdec):
        # 整数部分位数为输出位数减去输出小数位数(outlen)和小数点(1)
        print(f"{"#" * (outlen - outdec - 1)}.{"#" * outdec}")

    else:
        fin_int, fin_dec = numint, numdec
        # print(f"Going to deal with it normally.")
        # 首先针对小数部分进行处理，即四舍五入
        if len(numdec) > outdec: # 在存在小数位数比需求位数多的时候才判断"小数后那一位"
            if int(numdec[outdec]) >= 5: # 判断需求小数之后的那一位是否大于5，大于则四舍五入
                # print(numdec[:outdec])
                fin_dec = str(int(numdec[:outdec]) + 1)
                # print(f"Final decimals now {fin_dec}")

                if len(fin_dec) > outdec: # 此时+1之后位数改变，说明出现进位
                    if int(fin_int) >= 0:
                        fin_int = str(int(fin_int) + int(fin_dec[0])) # 用点蠢方法，正数进位为加，负数进位为减
                    else: fin_int = str(int(fin_int) - int(fin_dec[0]))
                    fin_dec = fin_dec[1:]
                    # print(f"进位! 当前fin_int {fin_int}, fin_dec {fin_dec}")

            else: 
                fin_dec = numdec[:outdec]
                # print(f"截选过后: {fin_dec}")
        # else:
            # print(f"小数位数本身已经满足需求位数, 不予处理")
        # print(f"The decimals out: {fin_dec}")
        
        final_out = fin_int + "." + fin_dec # 小数进行四舍五入之后就没啥可处理的了，直接接上
        if len(final_out) != outlen:
            final_out = "#" * (outlen - len(final_out)) + final_out # 这里因为经过筛选，大概率是输出总位数大于处理完的字符串位数了，直接按照差的位数补位即可
        print(final_out)
