"""
Input:
G1T B2S
Y1T Y3T B3O B3S R3O G3S G3T
Y1O B4T B1T Y4X B3T Y1X B1S B1X R1O
Output:
1 Y4X B3T

Input:
B4O Y
B3X B2X B2O Y3O G3O Y1X Y1O
Y3T G Y4T R1T 1 Y3X R3S G3S Y1T R4O Y2T 3 R R2T B1X R2X 2 R1O B3S B1S R1X R1S Y1S G1O G4S Y2O G1S B4X Y2S R4S G4O X T B4S R2O Y4S B3O R3O S R3X 4 B2S O Y4O B B4T G2T G3T
Output:
0 R2O G3T

**quick notes
1. 从手牌中找到最左侧一张与两张正面朝上卡牌中的其中一张相匹配的卡牌。将匹配的卡牌放置在那张正面朝上的卡牌上面，形成一个牌堆。
如果该卡牌与两张正面朝上的卡牌都匹配，则放在第一张卡牌上面。
-这里饶了一命, 用的是遍历算法, 我个人想法是用in判断, 不过比较麻烦的地方是万能牌就一个字符, 要用一下len不然肯定会out of range
--柠檬的好像不对啊哥们, 怎么一定要相似度2啊我操(修改)

2. 尝试将手中尽可能多的卡牌与该牌堆上的卡牌进行匹配。每次都从最左侧的卡牌开始查看。
-你怎么那么眼熟呢byd, 不过甚至要求每次从最左侧查看的话直接拿循环+break目光呆滞解决一切了(nmd还比23-24 C1容易, 什么逆天机制王超)
--我靠, 怎么那么奇怪啊这个机制, 目前看到的是刚好2个相似度才能放(修改); 同时如果是万能类卡牌的话会直接把它优先匹配上去
---你大爷, 要一直对那个第一次匹配的牌堆放, 我真是干了, 大修正大修正

3. 如果牌堆最上面是一张万能卡牌，则将与之匹配的第一张卡牌放在它上面。
-依旧是眼熟的要求, 一个优先匹配吧, 加个iswild就可以了(为啥叫wild啊老铁难不成万能牌很狂野么)
--好像就这个是难点?

4. 当手中没有卡牌或卡牌无法再继续匹配时，本轮游戏结束。
-回合终止条件吧, 我还是会用placed来判断

一轮游戏结束后，从抽牌堆中抽取尽可能多的纸牌，但手中持有的卡牌数不能超过 7 张。
然后进行下一轮游戏，直到手中和抽牌堆中没有卡牌，或者没有卡牌可以再继续匹配。
输出手中剩余卡牌的数量，后接每个牌堆最上面的卡牌。每张卡牌之间用一个空格隔开。
-这个抽牌有点(我就不赢我狂抽补满状态)的感觉, 不过反而是最简单的. 然后输出的话就需要记录咱们待放牌堆的牌了.
"""
"""
def placing_card_normal(targetcard0, targetcard1, placingcard):
    # 比较简单粗暴但是应该不会超时, 就是把准备放的卡每个元素查一下, 统计相似度再进行放置
    place_in_0, place_in_1 = 0, 0
    print(f"Now testing! checking {placingcard} with targets {targetcard0} and {targetcard1}.")

    for element in range(len(placingcard)):
        if placingcard[element] in targetcard0: # 与第一张牌有共同点
            print(f"There's similarity {placingcard[element]} with {targetcard0}")
            place_in_0 += 1
            # return [placingcard, targetcard1]
        
        if placingcard[element] in targetcard1: # 与第二张牌有共同点
            print(f"There's similarity {placingcard[element]} with {targetcard1}")
            place_in_1 += 1
            # return [targetcard0, placingcard]
    
    # 把相似度数据和其对应的放置位输出, 必须把所有相似度全部统计完才能判断哪个最适合放
    if place_in_0 == place_in_1 and place_in_0 == 0:# 没查到就返回空列表, 就是都没有任何的相同点
        return []
    
    if place_in_0 >= place_in_1: # 0号位相同点更多或与1号位有一样的相同点(优先放置于1号位)
        return [place_in_0, 0]
    
    elif place_in_1 > place_in_0: # 1号位相同点更多
        return [place_in_1, 1]

def placing_card_wild(targetcard0, targetcard1, placingcard):
    print(f"Now testing!(Wild) checking {placingcard} with targets {targetcard0} and {targetcard1}.")
    # 先看具体哪个是wild牌
    if len(targetcard1) == 1 and len(targetcard0) != 1:
        wild_index = 1
    else:
        wild_index = 0

    for element in range(len(placingcard)):
        if wild_index == 0 and placingcard[element] == targetcard0: # 0号位是wild, 而且对上准备放的牌的元素了
            return [2, wild_index]
        if wild_index == 1 and placingcard[element] == targetcard1: # 1号位是wild, 而且对上准备放的牌的元素了
            return [2, wild_index]
        # 有个有点抽象的思路, 就是在wild判断时期自动调高权重到2
    
    return [] # 如果都对不上的话那就不match, 推下一个
"""

def checkplacing(targetcard, placingcard): # 几乎是重做的修正, 把这个作为判断(相应的, 只会返回True/False)
    if len(targetcard) == 1 or len(placingcard) == 1: # 这个时候一定有一个是特殊牌
        if len(targetcard) == 1: # 准备放在特殊牌上
            return targetcard in placingcard # 如果目标在准备放的牌里那就是能放了, 返回一个True/False就可以了
        else:
            return placingcard in targetcard # 那就是特殊牌放上去, 查一下特殊牌有没有在目标牌的范围内就可以了
        
    similarity = 0
    for attribute in range(3): # 这里就肯定是正常牌放置在正常目标上了
        if placingcard[attribute] == targetcard[attribute]:
            similarity += 1
    
    return similarity == 2 # 一般来说就只有两项匹配才能放

# 经典list迅速接受数据
target_cards = list(input().split())
hand_cards = list(input().split())
draw_cards = list(input().split())

if len(target_cards[0]) == 1 or len(target_cards[1]) == 1: # 如果一开始就有特殊牌那就先设置wild
    iswild = True
else:
    iswild = False

break_testing_hand_cards = [-1] # 一个非常猎奇的判断是否需要结束的玩意, 用来对比本轮和上一轮的手牌差异, 如果没变说明完全放不了就会break
while hand_cards or draw_cards: # 手牌数大于0就持续跑(后续应该还要补条件)
    
    # 首先是放牌主循环, 最开始先把"匹配到就放"做出来, 遍历手牌的每一个查看是否与两个主牌堆匹配
    final_similarity, final_placing_index, final_hand_index = -1, -1, -1 # 开始查找下一个可以放的手牌之前先进行初始化
    curr_similarity, curr_placing_index, curr_hand_index = -1, -1, -1
    isplaceable = False
    
    for curr_card in range(len(hand_cards)): # 修正:这一步循环只用于寻找"第一个匹配的牌的牌堆"

        if checkplacing(target_cards[0], hand_cards[curr_card]):
            print(f"Find card {hand_cards[curr_card]} placing in index 0")
            final_placing_index = 0
            final_hand_index = curr_card
            isplaceable = True
            break
        
        elif checkplacing(target_cards[1], hand_cards[curr_card]):
            print(f"Find card {hand_cards[curr_card]} placing in index 1")
            final_placing_index = 1
            final_hand_index = curr_card
            isplaceable = True
            break
    
    if not isplaceable:
        print(f"No cards can be placed further. BREAK")
        break
        
        """
        if iswild: # 特殊牌另起一套处理出数据
            print(f"Going to place on wild card first, checking {hand_cards[curr_card]} now.")
            placing_results = placing_card_wild(target_cards[0], target_cards[1], hand_cards[curr_card])
        else: # 非特殊牌用常规处理出数据
            print(f"Placing card normally, checking {hand_cards[curr_card]} now.")
            placing_results = placing_card_normal(target_cards[0], target_cards[1], hand_cards[curr_card])
        
        if len(placing_results) > 0: # 长度大于0代表有效数据输出, 可以进行下一步操作
            curr_similarity, curr_placing_index = placing_results[0], placing_results[1]
            curr_hand_index = curr_card
            print(f"Find valid data with similarity {curr_similarity} and placing index {curr_placing_index}")

            if curr_similarity > final_similarity: # 发现了相似度更高的数据组, 进行更新
                final_similarity, final_placing_index = curr_similarity, curr_placing_index
                final_hand_index = curr_hand_index

            if final_similarity == 2: # 操作更新之后专门查一遍看看是否有出现相似度为2的牌可以放置, 就可以直接退出查牌循环了
                print(f"Find card {hand_cards[final_hand_index]} placing in index {final_placing_index}.")
                isplaceable = True
                break

        if curr_similarity == len(hand_cards[curr_hand_index]): # 当前正在查的卡牌完全匹配(这步处理到特殊卡的话会加一个len判断)随后立即更新
            print(f"The card {hand_cards[curr_hand_index]} completely matches the target card {target_cards[curr_placing_index]} index {curr_placing_index}")
            final_similarity, final_placing_index = curr_similarity, curr_placing_index
            final_hand_index = curr_hand_index
            isplaceable = True

            if len(hand_cards[curr_hand_index]) == 1: # 这个我还额外加判断条件吧, 就是如果这玩意完美匹配并且匹配手牌长度为1那他就是可放置的特殊牌(wild)
                print(f"Finding a wild card.")
                iswild = True
            break

        print(f"For now, the index position {final_placing_index} will be placed, the highest similarity {final_similarity} now in total.")
        """
    # 到这里就跑完一次"把手牌全过一遍"循环了, 开始处理实际放置
    # print(f"Now supposed to be placing {hand_cards[final_hand_index]} into position {final_placing_index}!")

    # 纯粹为了测试, 把我更新的target开个新表存一下, 再进行更新
    if isplaceable: # 注意只在可以放的时候放(相似度为2/特殊牌)

        # 大修正: 到这一步会拿到第一个匹配的目标牌index和第一个匹配对应的手牌index

        updated_target_cards = []
        if final_placing_index == 0:
            updated_target_cards = [hand_cards[final_hand_index], target_cards[1]]
        else:
            updated_target_cards = [target_cards[0], hand_cards[final_hand_index]]

        print(f"targets updated {updated_target_cards}")
        # 把表格更新一下, 顺便把出出去的牌pop了
        target_cards = updated_target_cards
        hand_cards.pop(final_hand_index)
        print(f"hand updated {hand_cards}")

        # 大修正: 到这里可以进循环开始继续找匹配的牌
        while isplaceable:
            isplaceable = False

            for curr_card in range(len(hand_cards)):
                if checkplacing(target_cards[final_placing_index], hand_cards[curr_card]): # 一模一样的判定不过只需要聚焦一个
                    final_hand_index = curr_card
                    isplaceable = True
                    break
            
            if isplaceable: # 这个其实也是重复代码照搬吧
                updated_target_cards = []
                if final_placing_index == 0:
                    updated_target_cards = [hand_cards[final_hand_index], target_cards[1]]
                else:
                    updated_target_cards = [target_cards[0], hand_cards[final_hand_index]]

                print(f"PLACING targets updated {updated_target_cards}")
                # 把表格更新一下, 顺便把出出去的牌pop了
                target_cards = updated_target_cards
                hand_cards.pop(final_hand_index)
                print(f"PLACING hand updated {hand_cards}")
        """
        if len(target_cards[0]) == 1 or len(target_cards[1]) == 1: # 再查一遍看有没有wild
            iswild = True
        else:
            iswild = False
        
        # 修正:可能会要在这里再加一个循环来处理放牌, 已经得到了要放在的地方之后对着那里查就可以了
        # 这一块专门用来放牌, 所以可能会有大量重复代码
        while isplaceable:
            curr_similarity, curr_placing_index, curr_hand_index = -1, -1, -1
            isplaceable = False

            for curr_card in range(len(hand_cards)): # 其实我就直接照搬了, 但是效率会下降因为有重复检验
                # 本质上这一段内循环是为了"找到符合要求的牌"并"立刻退出该循环进行放置"

                if iswild: # 特殊牌另起一套处理出数据
                    print(f"PLACING Going to place on wild card first, checking {hand_cards[curr_card]} now.")
                    placing_results = placing_card_wild(target_cards[0], target_cards[1], hand_cards[curr_card])
                else: # 非特殊牌用常规处理出数据
                    print(f"PLACING Placing card normally, checking {hand_cards[curr_card]} now.")
                    placing_results = placing_card_normal(target_cards[0], target_cards[1], hand_cards[curr_card])
                
                if len(placing_results) > 0: # 长度大于0代表有效数据输出, 可以进行下一步操作
                    curr_similarity, curr_placing_index = placing_results[0], placing_results[1]
                    curr_hand_index = curr_card
                    print(f"PLACING Find valid data with similarity {curr_similarity} and placing index {curr_placing_index}")

                    if curr_placing_index == final_placing_index and curr_similarity == 2: # 查牌发现了一样的放牌位置会准许放置(这里也会有一大块重复的放置用代码)
                        print(f"Going to place!")
                        isplaceable = True
                        break
                
                if curr_similarity == len(hand_cards[curr_hand_index]) and curr_placing_index == final_placing_index: # 当前正在查的卡牌完全匹配(这步处理到特殊卡的话会加一个len判断)随后立即更新
                    print(f"PLACING The card {hand_cards[curr_hand_index]} completely matches the target card {target_cards[curr_placing_index]} index {curr_placing_index}")
                    isplaceable = True

                    if len(hand_cards[curr_hand_index]) == 1: # 这个我还额外加判断条件吧, 就是如果这玩意完美匹配并且匹配手牌长度为1那他就是可放置的特殊牌(wild)
                        print(f"PLACING Finding a wild card.")
                        iswild = True
                    break
            
            # 出循环之后如果是可放置的话那就进行放置操作
            if isplaceable: # 注意只在可以放的时候放(相似度为2/特殊牌)

                updated_target_cards = []
                if final_placing_index == 0:
                    updated_target_cards = [hand_cards[curr_hand_index], target_cards[1]]
                else:
                    updated_target_cards = [target_cards[0], hand_cards[curr_hand_index]]

                print(f"PLACING {updated_target_cards}")
                # 把表格更新一下, 顺便把出出去的牌pop了
                target_cards = updated_target_cards
                hand_cards.pop(curr_hand_index)
                print(f"PLACING {hand_cards}")

                if len(target_cards[0]) == 1 or len(target_cards[1]) == 1: # 再查一遍看有没有wild
                    iswild = True
                else:
                    iswild = False

        # if iswild and not isplaceable: # 在这里(可以放置在特殊牌上方)进行状态重置
            # iswild = False
        # 这里弄完之后赶紧回去检查看有没有其他牌可以place上去不然有点完蛋
        continuing_placing = False # 检测看还能不能放了
        for curr_card in range(len(hand_cards)):
            if iswild: # 特殊牌另起一套处理出数据
                print(f"Going to place on wild card first, checking {hand_cards[curr_card]} now.")
                placing_results = placing_card_wild(target_cards[0], target_cards[1], hand_cards[curr_card])
            else: # 非特殊牌用常规处理出数据
                print(f"Placing card normally, checking {hand_cards[curr_card]} now.")
                placing_results = placing_card_normal(target_cards[0], target_cards[1], hand_cards[curr_card])
            
            if len(placing_results) > 0: # 长度大于0代表有效数据输出, 可以进行下一步操作
                curr_similarity, curr_placing_index = placing_results[0], placing_results[1]
                curr_hand_index = curr_card
                print(f"Find valid data with similarity {curr_similarity} and placing index {curr_placing_index}")

                if curr_similarity == 2:
                    continuing_placing = True # 依然有牌匹配, 别进抽牌程序
                    break

            if curr_similarity == len(hand_cards[curr_hand_index]) and len(hand_cards[curr_hand_index]) == 1: # 特殊牌
                continuing_placing = True # 本质上这只是简单看谁能place的, 不需要任何额外判断(就是重复代码有点多)
                break
        
        if continuing_placing:
            continue # 简易判断
        # continue # 本质上如果可以放那就放了, 然后继续查看哪个牌可以放, 下面就是抽牌阶段
    """
    # 能跑到这里那说明需要去抽牌了
    # 修正: 事实上这一段是必须在每次的while里跑到的, 抽牌代表"这一局游戏结束"
    # 再修正: 不到抽牌时刻别进去
    print(f"Going to draw, as no cards with similarity higher than 2 appears. Actually, a game turn has finished.")

    # if len(draw_cards) == 0 or len(hand_cards) == 7: # 准备抽牌发现没牌了或者手牌满了, 那就说明没有任何牌可以放了, 跳出放牌循环准备收尾
        # print(f"There's no cards that can be further placed / draw. targets {target_cards} and hand cards {hand_cards}")

        # if break_testing_hand_cards == hand_cards or len(hand_cards) == 7:
    """
            if iswild:
                print(f"Wild may have stuck it. Try again?")
                iswild = False
                continue # 这是一个万不得已的方法, 就是如果因为wild导致有些能放的被卡了那就把卡住的wild删掉再试一遍
    """
            # print(f"The hand cards {hand_cards} doesn't change (last one {break_testing_hand_cards}) // hand cards are full. END")
            # 如果手牌对比上一轮没变过或者手牌满了就会break
        # break

        # else: # 如果不一样我就记上一轮的手牌样子
            # break_testing_hand_cards = hand_cards

    while len(hand_cards) < 7 and draw_cards: # 本质上算是补满手牌, 但是前提是抽牌堆还有牌
        print(f"Putting {draw_cards[0]} into hand {hand_cards}")
        hand_cards.append(draw_cards.pop(0))
    
    print(f"After drawing, hand cards {hand_cards} and draw cards {draw_cards}")
    # break # 2026-1-17 23:00老子踏马的整了60多行终于放下了第一张牌，澡称冯福

print(f"Done main process, hand {hand_cards}, targets {target_cards}")
print(f"{len(hand_cards)} {target_cards[0]} {target_cards[1]}")
