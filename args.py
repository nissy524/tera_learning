def func(*args):
    result=','.join(args)
    print(result)

func('あ')
func('あ','A','a')
#可変長引数のあとに引数を書く際は、x=がいる
def func(x,*args):
    print(args)
    print(x)
func(1,'a','b','c')

def func(*args, x):
    print(args)
    print(x)
func('a','b','c',x=1)

def func(*args,x):
    result=','.join(args)
    print(f'{x}:{result}')

func('あ',x=1)
func('あ','A','a',x=2)


def func(x,**kwargs):
    print(f'{x}:{kwargs}')


func(1,name='斎藤',user_id=222)
func(2,item='牛乳',item_id=111,price=100)



