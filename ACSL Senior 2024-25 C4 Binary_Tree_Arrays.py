"""
Input:
GASTON

Output:
1 0 3 9 21

**quick notes
由字符串 GASTON 构建的二叉搜索树如右图所示. 该数据结构可通过以下三个数组表示：
* 一个按字符串中出现顺序存储键的数组
* 一个数组记录每个键左子节点的位置
* 一个数组记录每个键右子节点的位置

插入新键时, 需确定其在树中的位置, 并将其父节点左子数组或右子数组的值更新为新键的位置.
若左子数组或右子数组中的值为 -1, 则表示该节点对应的子节点不存在.

以下是由字符串 GASTON 生成的三个数组：
        0  1  2  3  4  5 …
键      G  A  S  T  O  N
左子节点 1 -1  4 -1  5 -1
右子节点 2 -1  3 -1 -1 -1
- 这就是经典的二叉搜索, 但是他用了个链表结构来存整个树, 左右指针分别去指向每个节点.
- 用多层来套比较容易混, 不过这算是我想到的一种思路吧?

本程序将提供一个字符串, 你需要根据其字母来构建二叉搜索树. 树构建完成后, 请为每棵树找出以下信息：
* 仅含左子节点的节点数、仅含右子节点的节点数、叶节点数、内部路径长度和外部路径长度.
将这 5 个数值以字符串形式输出, 各数值之间用单个空格分隔.
- 这些为了防止混淆, 尽量还是在把树建好了之后再单独去弄吧
"""
tree_str = input()
tree = []
for i in range(len(tree_str)):
    curr_ch = tree_str[i]
    curr_node = [curr_ch, -1, -1, 0] # 造一个内嵌链表, [1]是左侧指针, [2]是右侧指针, [3]用来记录当前在哪一层
    tree.append(curr_node)
    print(f"Added node {curr_node}")

    if len(tree) > 1: # 树的内部有大于一个节点, 那之后的节点都是插入的, 需要进行对比
        compared_index = 0 # 专门用来对比的index
        depth = 1
        get_position = False
        while not get_position:
            print(f"comparing {curr_node} with tree {tree[compared_index]}")

            if curr_ch <= tree[compared_index][0]: # 这个时候先查左边是不是空的, 再决定是否停止
                print(f"Going to the left.")
                
                if tree[compared_index][1] == -1: # 左边是空的, 那就在那个方向更新指针
                    print(f"can be placed at left of tree {tree[compared_index]}!")
                    tree[compared_index][1] = i
                    tree[i][3] = depth
                    get_position = True

                else: # 左边有东西的话更新一下目前准备对比的index
                    compared_index = tree[compared_index][1]
                    depth += 1

            else: # 右边比左边大那一定是查节点右侧
                print(f"Going to the right.")

                if tree[compared_index][2] == -1: # 右侧为空
                    print(f"can be placed at right of tree {tree[compared_index]}!")
                    tree[compared_index][2] = i
                    tree[i][3] = depth
                    get_position = True

                else: # 右边有东西的话更新一下目前准备对比的index
                    compared_index = tree[compared_index][2]
                    depth += 1
        
print(f"Completed tree {tree}")

# 测试正常, 接着可以开始找需要的值
left_count, right_count, leaf_count, internal_len, outter_len = 0, 0, 0, 0, 0
for j in range(len(tree)):
    left, right, depth = tree[j][1], tree[j][2], tree[j][3]

    if left != -1 and right == -1: # 对应只包含左节点的
        left_count += 1
    if left == -1 and right != -1: # 对应只包含右节点的
        right_count += 1
    if left == -1 and right == -1: # 两边都没有就是叶节点
        leaf_count += 1
    
    # 内部路径得数这个节点的left和right, 怎么感觉好像有四种情况?
    # 这里写一下: 每一个-1都会给外部路径增加深度+1, 每个节点指针会给内部路径增加深度+1(数它到底下节点的长度所以+1)
    if left == -1:
        print(f"the {tree[j]} has left outer len {depth + 1}")
        outter_len += depth + 1
    if left != -1:
        print(f"the {tree[j]} has left internal len {depth + 1}")
        internal_len += depth + 1
    if right == -1:
        print(f"the {tree[j]} has right outer len {depth + 1}")
        outter_len += depth + 1
    if right != -1:
        print(f"the {tree[j]} has right internal len {depth + 1}")
        internal_len += depth + 1

print(left_count, right_count, leaf_count, internal_len, outter_len)
