"""
Input:
102438 3
4329 1
6710 2
16807 1
60098065452 7
Output:
546414
1312113
7841
8131571
1488173823436
"""
def isprime(num): # 快速搓一个判断质数
    if num == 1:
        return 0 # 1不是质数，返回False
    
    div = 2
    while div ** 2 <= num: # 一个边界提速的方法，由于合数的因数都是成对/平方单个出现，一般在div平方小于num的时候来判断效率比较高
        if num % div == 0:
            return 0
        div += 1
    
    return 1

def count_prime_factor(num): # 计算一个数的总质因数个数，底层逻辑和边界设置和isprime()其实差不太多
    if num == 1:
        return 0 # 1没有质因数，他自己都不是质数
    
    div = 2
    sum = 0
    sum += isprime(num) # 比较容易漏的一点，如果这个数是质数，那么他的质因数是他自己
    while div ** 2 <= num:
        if num % div == 0: # 能整除的话立马出1/2个因数扔进去处理
            sum += isprime(div)
            if div ** 2 != num: # 不是平方数的根，就再扔一个去判断
                sum += isprime(num // div)
        
        div += 1
    
    return sum

for _ in range(5):
    num, pos = input().split()
    pos = int(pos)
    numout = ""
    for i in range(-1, -len(num) - 1, -1): # 下界还是要再拓一格出去，不然覆盖不到首位
        print(f"Dealing with {num[i]}")
        # 分别处理之后接在字符串前面，分三段(-1到-pos，-pos和-pos到-len(num))
        if i == -pos:
            print(f"number of prime factors ({count_prime_factor(int(num))}) is added to {numout}")
            numout = str(count_prime_factor(int(num))) + numout
        elif i < -pos:
            print(f"number ({int(num[i]) + int(num[-pos])}) is added to {numout}")
            numout = str(int(num[i]) + int(num[-pos])) + numout
        else:
            print(f"number ({abs(int(num[i]) - int(num[-pos]))}) is added to {numout}")
            numout = str(abs(int(num[i]) - int(num[-pos]))) + numout

        print(f"The number output is now like {numout}")

    print(numout)
