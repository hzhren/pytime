'''
将华氏温度转换为摄氏温度
'''
f = float(input('请输入华氏温度: '))
c = (f - 32) / 1.8
print('%.1f华氏度 = %.1f摄氏度' % (f, c))

"""
输入半径计算圆的周长,面积,表面积,体积。
"""
radius = float(input('请输入圆的半径: '))
perimeter = 2 * 3.1416 * radius
area = 3.1416 * radius * radius
a = 4*3.1416*radius*radius
v = 4/3*3.1416 * radius * radius* radius
print('周长: %.2f' % perimeter)
print('面积: %.2f' % area)
print(f'表面积: {a}')
print('体积: %.2f' %v)