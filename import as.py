import numpy as np
x=np.array([1,2,3])
y=np.array([10,11,12])
print(x+y)
# import A as BでimportしたAをBに略したことになる

with open('horse.ini')as h:
    s= h.read()
    print(s)

with open('horse.ini')as h:
    for _ in range(2):
        s_line=h.readline()
        print(s_line)

with open('horse.ini')as h:
    for _ in range(5):
        s_line=h.readline()
        print(s_line)
        if s_line =='':
# 上記は空の変数を反転させるものもの
            print('終了です')

x_set= {11,222,333}
y_list=[11,333,444,555,11]
y_set=set(y_list)

result=x_set|y_set
print(result)

x_tuple=(1,3,5)
y_list=[3,4,5]
y_tuple=tuple(y_list)

result=x_tuple[2]
print(result)

def test_function():
    x=2*2
    y=3*3
    return x,y

result1=test_function()
print(result1)

x_dict={'a':100,'b':200,'c':300}
for (x,y) in x_dict.items():
    print(x)
    print(y)

age=0
result='成人' if age>=20 else'子供'if age>=1 else'赤ちゃん'
print(result)







