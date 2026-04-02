"""
Input:
E 3 7 h ACSL Sr-5 c2
E 0 1 s Python Programming is easier than programming in Java.
D 2 5 j 396 404 447 472 329 380 381 341 423 411 436 408 474 428 383 405 414 431 332 437 474 485 347 407 453 377 430 459 471 421 401 353 413 446 456 424 392 457 447 441 419 435 413 442 330
E 7 10 a Fibonacci Numbers are found in many places including the Mandelbrot Set.
D 6 1 z 379 479 341 447 448 329 381 397 402 402 395 462 404 383 425 434 446 383 469 468 405 464 408 449 433 329 390 425 429 395 446 420 449 368 417 397 363 363 395 429 443 383 464 395 446 344 408 458 445 431 335 367 402 394 475 419 391

Output:
386 358 425 415 347 419 405 402 377 377 390 416
425 463 464 443 465 440 323 386 444 432 457 426 406 457 415 414 452 415 329 465 475 377 461 427 412 405 443 417 338 458 413 397 464 323 442 420 402 463 468 448 457 457 450 458 445 383 441 470 353 380 457 409 433 346
Help ME figure out how to solve this problem!
382 444 440 477 455 409 423 456 441 344 393 483 427 437 449 474 472 326 451 423 437 374 465 459 423 443 442 392 456 410 374 436 403 422 484 350 448 459 451 465 458 415 380 426 428 393 423 465 436 408 434 451 377 410 446 422 344 377 400 476 406 452 432 416 411 423 470 359 401 401 425 406
It is 9:30 in the morning EST but 6:30 on the West Coast.
**quick notes
-逆天解码/加密集成程序,怎么说呢如果用def的话def里面会特别长,我可能会用if/else来分.

1. 找出与该字符具有相同索引的斐波那契数（如根据以上数列,第一个字符用数字3来表示,第五个字符用数字27来表示.)
-也就是说, 得新增一个专门用来写斐波那契的def

2. 根据输入密钥,找出对步骤 1 中斐波那契数进行偏移操作的新字母。必要时可以再
次使用字母表开头的新字母(如假设密钥是"p",斐波那契数是17,那么新的字母
即为"g")。
-这个一大坨懒得看, 就是直接加/减当前对应的那个数来进行偏移.

3. 通过将字符串中该字符的ASCII代码与步骤2中该字母的ASCII代码的3倍相加,即
可获得每个字符的数字编码。
-这个就是说上面算的是字母ASCII, 我个人感觉可以把它当查验方法. 就是有效的字母ASCII查验, 有效就把它乘3加原来字母ASCII变成加密数字.

hint 1) 从字符串上的第1个字符起,在奇数位置上的字符将转变为右边的字符;从第2个字
符起,偶数位置上的字符将转变为左边的字符。
-这个简单, 奇数用加偏移, 偶数用减偏移

hint 2) 在每次输入的开始,会有一个另外的大写字母(E 表示编码,D 表示解码）。需要编
码时,会提供信息。需要解码时,会提供字符串,中间由空格隔开.
-阴,老子就玩个加密你还要我解密
"""
def next_fib(fib1, fib2):
    return fib1 + fib2

for _ in range(5):
    method, fib1, fib2, key, text_dealing = input().split(" ", 4)
    fib1, fib2 = int(fib1), int(fib2)
    printed = False
    alpha_list = "abcdefghijklmnopqrstuvwxyz"
    test_output = ""
    if method == "E":
        # print("Encoding message...")
        # 不需要进行多余定义, 始终使用fib1作为当前处理的fib数

        key_ascii = ord(key)
        for i in range(len(text_dealing)):
            # print(f"encoding ascii will be {key_ascii} + {fib1} now.")
            # 判断奇偶在循环内相反, 偶数会余1, 奇数余0; 在此处进行移位操作而非后面
            if i % 2 == 0: # 奇数用加移位
                enc_ascii = alpha_list.find(key) + fib1
                # enc_ascii = key_ascii + fib1
            elif i % 2 != 0: # 偶数用减移位
                enc_ascii = alpha_list.find(key) - fib1
                # enc_ascii = key_ascii - fib1
            
            # 计算出加密要乘三加上去的数的初版之后立刻推进fib不然忘了
            fib1, fib2 = fib2, next_fib(fib1, fib2)

            # 接下来处理一下准备乘三的加密ascii数, 我直接用笨办法(少了就加26多了就减26)
            # print(f"currently, the encoding ascii is {enc_ascii}")

            # 我靠, 数大起来你这byd时间太长了肯定跑超时, 还是得用余数
            """
            while not (enc_ascii >= 97 and enc_ascii <= 122):
                if enc_ascii < 97: enc_ascii += 26
                if enc_ascii > 122: enc_ascii -= 26
            """
            enc_ascii %= 26 # 这一步能快速找出处理后当前的字母的索引
            enc_ascii = ord(alpha_list[enc_ascii]) # 用索引把字母对应上再转ascii

            # 得到最终加密用数, 可以把它乘三加上/减去当前字符ascii数.
            # print(f"Get final encoding ascii {enc_ascii}")
            curr_ascii = ord(text_dealing[i])
            outnum = curr_ascii + 3 * enc_ascii
            
            test_output += str(outnum) + " "
            # 智人操作: 第一次不打空格, 之后打空格
            # if printed == False:
                # print(f"Getting number {outnum}")
                # print(outnum, end = "")
                # printed == True
            # elif printed:
                # print(f"Getting number {outnum}")
                # print(f" {outnum}", end = "")
        print(f"Final output: {test_output[:-1]}")

    elif method == "D":
        # 解码我得研究下
        # print("Decoding message...")

        text_dealing = list(text_dealing.split())
        key_ascii = ord(key)
        for i in range(len(text_dealing)):
            # print(f"encoding ascii will be {key_ascii} + {fib1} now.")
            # 判断奇偶在循环内相反, 偶数会余1, 奇数余0; 在此处进行移位操作而非后面
            if i % 2 == 0: # 奇数用加移位
                enc_ascii = alpha_list.find(key) + fib1
                # enc_ascii = key_ascii + fib1
            elif i % 2 != 0: # 偶数用减移位
                enc_ascii = alpha_list.find(key) - fib1
                # enc_ascii = key_ascii - fib1
            
            # 计算出加密要乘三加上去的数的初版之后立刻推进fib不然忘了
            fib1, fib2 = fib2, next_fib(fib1, fib2)

            # 接下来处理一下准备乘三的加密ascii数, 我直接用笨办法(少了就加26多了就减26)
            # print(f"currently, the encoding ascii is {enc_ascii}")

            # 我靠, 数大起来你这byd时间太长了肯定跑超时, 还是得用余数
            """
            while not (enc_ascii >= 97 and enc_ascii <= 122):
                if enc_ascii < 97: enc_ascii += 26
                if enc_ascii > 122: enc_ascii -= 26
            """
            enc_ascii %= 26 # 这一步能快速找出处理后当前的字母的索引
            enc_ascii = ord(alpha_list[enc_ascii]) # 用索引把字母对应上再转ascii

            # 得到最终加密用数, 可以把它乘三加上/减去当前字符ascii数.
            # print(f"Get final encoding ascii {enc_ascii}")
            # 啊哈哈哈我逃课直接复制, 其实原理一样只不过这次算出来要进行返还
            outnum = int(text_dealing[i]) - 3 * enc_ascii
            test_output += chr(outnum)
        print(f"Final output: {test_output}")
