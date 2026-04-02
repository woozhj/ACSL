"""
Input:
5D, 2D, 6H, 9D, TD, 6H
TC, AC, KC, QH, JS, TD
3D, 4H, 5C, 6S, 2D, 7H
KS, TH, QC, 3D, 9H, 3H
AC, AD, KH, AS, KS, QS
Output:
9D
KC
2D
3D
AD 
"""
for _ in range(5):
    cards = list(input().split(", "))
    lead = cards.pop(0)
    rank_order = "A23456789TJQK" # 打个表吧，字符串也是表怎的
    suit_order = "CDHS" # 你好我打两个

    # 先进行第一层判断，也就是"庄家有没有相同suit的牌?"
    least_index = -1 # 这个是用来寻找"相同suit内点数最小"的牌
    target_index = -1 # 这个是用来寻找"相同suit且刚好比lead点数大"的牌
    least_rank_index = -1 # 这个是用来寻找"拥有最小点数和最小suit"的牌，此时会用rank_order和suit_order来分别判断

    for i in range(5): # 由于庄家一定是5张牌，就不必再使用len()了
        print(f"Checking {cards[i]}")
        cur_rank, cur_suit = cards[i][0], cards[i][1]

        if least_rank_index < 0 or (rank_order.index(cur_rank) < rank_order.index(least_rank)):
            # 第一次寻找默认把第一张手牌定作点数最小手牌;如果当前手牌拥有更小点数则更新点数最小手牌的索引
            least_rank_index = i
            least_rank, least_suit = cur_rank, cur_suit
            print(f"Find the least total rank {cards[least_rank_index]}")
        elif rank_order.index(cur_rank) == rank_order.index(least_rank) and suit_order.index(cur_suit) < suit_order.index(least_suit):
            # 出现了当前手牌点数和点数最小手牌点数相同的情况，加入花色大小判断
            least_rank_index = i
            least_rank, least_suit = cur_rank, cur_suit
            print(f"Find the least total rank {cards[least_rank_index]}")

        # 这里我得解释一下为什么上面不使用rank和suit当作权重来计算最小权重，因为如果出现AS和2C这种情况下应当打出AS(数字最小)，但是按照权重计算的话2C将会被打出(2C的1比AS的3更小)

        if suit_order.index(cur_suit) == suit_order.index(lead[1]): # 庄家有相同suit的牌
            print(f"Find {cards[i]} with same suits with {lead}")
            
            if least_index < 0 or (rank_order.index(cur_rank) < rank_order.index(cards[least_index][0])):
                # 第一次找到相同suit默认定为最小;如果当前手牌点数比least小则更新least
                least_index = i
                print(f"Find the least rank {cards[least_index]}")
            
            if rank_order.index(cur_rank) > rank_order.index(lead[0]): # 庄家的这个牌点数比对手的牌点数大，开始寻找target
                if target_index < 0 or (rank_order.index(cur_rank) < rank_order.index(cards[target_index][0])):
                    # 第一次找到点数比对手大的牌默认定为target;如果当前手牌点数比target小则更新target
                    target_index = i
                    print(f"Find the target rank {cards[target_index]}")

    if target_index > 0:
        print(f"Plays target {cards[target_index]}")
    elif least_index > 0:
        print(f"Plays least {cards[least_index]}")

    else:
        print(f"Plays total least {cards[least_rank_index]}")
