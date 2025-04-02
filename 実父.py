sales_2020=[400239,560213,542490]
sales_2019=[489028,400123,442489]

for current,previous in zip (sales_2020,sales_2019):
    result=(current/previous-1)*100
    print(f'{result:.1f}%')
#2つ比較対象があるとき、数が合わなかったら少ないほうが終わり次第for文は終わる

names=['寺下','鈴木','戸部']
for i, n in enumerate(names, start=1):
    print(f'{i}位:{n}')

a=lambda x,y:print(f'{x}さんは{y}です')
a('てらした','いけだ')

a1=['寺下','鈴木','戸部']
a2=['かずき','まさき','ゆうき']
result=list(map(lambda x,y:x+y+'さん',a1,a2))
print(result)

numbers=[5,8,10,12,30]
result=list(filter(lambda x:x>=10,numbers))
print(result)


