"""
Input:
0, 5, 2, 6
1, 7, 3, 0
2, 4, 1, 5
4, 2, 3, 4
4, 5, 6, 7
Output:
101 010 110 and r-x -w- rw-
111 011 000 and rws -wx ---
100 001 101 and r-- --s r-x
010 011 100 and -w- -wx r--
101 110 111 and r-x rw- rwt

**quick notes
0 - no spec
1 - owner
2 - group
4 - others
spec => (owner / group) x -> s; (others) x -> t
"""
def den_to_bin(num):
    num = int(num)
    bin_num = ""
    while num != 0: # number在被处理到为0时停止
        bin_num = str(num % 2) + bin_num # 从前面开始接入num对2的余数
        num //= 2  
    return bin_num

def quick_trans(user_class):
    permission = ""
    permission_list = "rwx" # 依旧打表起手，不过这个表只适用于基础，特殊权限后期单独处理
    for i in range(3):
        if user_class[i] == "1": # 根据user_class的具体为1的位来把默认无权限(-)转为对应默认权限
            permission += permission_list[i]
        else: permission += "-"
    return permission

for _ in range(5):
    spec, u, g, o = map(int, input().split(", "))

    # user_class逐个转换，注意由于部分数二进制少一位e.g. 2变为10而非010，所以要再zfill一下子
    user = den_to_bin(u).zfill(3)
    group = den_to_bin(g).zfill(3)
    others = den_to_bin(o).zfill(3)
    # user_class对应权限逐个转化
    user_per = quick_trans(user)
    group_per = quick_trans(group)
    others_per = quick_trans(others)
    # 每个user_class再根据特殊权限进行单独修改，我直接堆叠if了
    if spec == 1 and user_per[-1] != "-":
        user_per = user_per[:2] + "s"

    if spec == 2 and group_per[-1] != "-":
        group_per = group_per[:2] + "s"

    if spec == 4 and others_per[-1] != "-":
        others_per = others_per[:2] + "t"

    print(f"{user} {group} {others} and {user_per} {group_per} {others_per}")
