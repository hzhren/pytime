"""
用for-in实现1-365的求和
versoin 0.1
"""
total=0
for i in range(1,366):
    total+=i
print(total)

"""
打印乘法口诀表

Version: 0.1
Author: 骆昊
"""
for i in range(1, 10):
    for j in range(1, i + 1):
        print(f'{i}x{j}={i * j}', end='\t')
    print()

"""
用while实现1-100内猜数字游戏
"""
import random
answer=random.randint(1,300)
counter=0
while True:
    counter+=1
    number=int(input('请输入：'))
    if number>answer:
        print('你输入的数字大了！')
    elif number<answer:
        print('你输入的数字小了')
    else:
        print('恭喜你输入正确！')
        break
print(f'你一共输入了{counter}次')