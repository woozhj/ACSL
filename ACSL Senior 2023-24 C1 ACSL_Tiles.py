"""
Input:
5923
56 27 73 34 99 45 32 17 64 57 18 11
36 92 22 50 82
Output:
16
"""
def is_placeable(tile, target):
    if tile[0] == target: # 查一遍首位和末位，相同表示可以放置，返回另一位
        return tile[1]
    if tile[1] == target:
        return tile[0]
    return ""

target_tiles = list(map(str, input().zfill(4))) # 目标牌，zfill确保长度为4
hand_tiles = list(map(str, input().split()))
draw_tiles = list(map(str, input().split()))

target_pivot = 0 # 标记当前等待放置的target_tiles
is_double = False
# failed_times = 0 # 记录连续未能放置的次数
while len(hand_tiles) > 0:
    placed = False

    for i in range(len(hand_tiles)):
        for _ in range(4):
            # 把手牌每一张去和目标牌的每一位做对比，寻找可放置的牌
            hand_tiles[i] = hand_tiles[i].zfill(2)
            place_tile = is_placeable(hand_tiles[i], target_tiles[target_pivot])
            print("Checking tiles: ", hand_tiles[i], target_tiles[target_pivot], place_tile)

            if len(place_tile) > 0:
                # 可以放置。
                # failed_times = 0 # 重置失败次数

                print(f"placing {hand_tiles[i]} on {target_tiles[target_pivot]}")
                target_tiles[target_pivot] = place_tile # 更新目标牌
                is_double = (hand_tiles[i][0] == hand_tiles[i][1]) # 检测特殊手牌
                hand_tiles.pop(i) # 从手牌中移除

                print(f"After placing, the targets: {target_tiles}")
                print("The tiles now looks like: ", hand_tiles, target_tiles)

                if not is_double:
                    # 此时为非特殊手牌，可以继续往下推进target_pivot
                    target_pivot = (target_pivot + 1) % 4
                
                placed = True # 更新已放置标记
                break

            # failed_times += 1 # 照理说走到这多半是没放成功，失败次数先+1
            if is_double: # double情况会固定指针停止推进
                break
            
            target_pivot = (target_pivot + 1) % 4 # 推进target_pivot，继续尝试
        
        if placed: # 检测到已放置，跳出当前遍历手牌循环
            break
    
    if not placed: # 到这一步应该是遍历完手牌也找不到可以放的，开始抽牌
        print("Going to Draw.")
        # break
    
    if len(draw_tiles) == 0 and not placed:
        print("Cannot draw. Game complete.")
        break # 此时想要抽牌但是没牌了，结束

    # 运行到这里应该代表需要抽牌了，开始抽牌程序
    while len(draw_tiles) > 0 and not placed:
        hand_tiles.append(draw_tiles.pop(0)) # 抽牌
        print(f"checking draw tile {hand_tiles[-1]} with {target_tiles[target_pivot]}")

        for _ in range(4):
            print(f"checking {hand_tiles[-1]} to {target_tiles[target_pivot]}")

            hand_tiles[-1] = hand_tiles[-1].zfill(2)
            place_tile = is_placeable(hand_tiles[-1], target_tiles[target_pivot])
            if len(place_tile) > 0: # 可以被放置
                print(f"place {hand_tiles[-1]} to {target_tiles[target_pivot]}")
                target_tiles[target_pivot] = place_tile
                placed = True
                is_double = (hand_tiles[-1][0] == hand_tiles[-1][1])
                hand_tiles.pop(-1)
                
                print(f"After placing, the targets are: {target_tiles}")
                print("The tiles now looks like this: ", hand_tiles, target_tiles)

                if not is_double:
                    target_pivot = (target_pivot + 1) % 4
                
                break
                
            if is_double:
                break # double 立刻推进

            target_pivot = (target_pivot + 1) % 4
        
    print("Drawing complete.")

    if not placed:
        print("Game completed. No tiles can be placed further.")
        print(f"The hand tiles: {hand_tiles} and target: {target_tiles}")
        break

print(f"The left hand tiles: {hand_tiles}")

sum = 0
for i in hand_tiles:
    sum += int(i[0]) + int(i[1])
print(sum)
