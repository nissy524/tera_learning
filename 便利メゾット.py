file_name='2nd_term_student.csv'
if file_name.startswith('2nd'):
    print('２学期のデータです')
    with open(file_name)as f:
        x=f.readlines()
        

#replace 文字列のある部分を別の文字に置き換える
x='keiba_titleholder_and_keiba_karate'
y=x.replace('keiba','uma')
print(y)
# y=x.replace('keiba_','')でkeibaを削除できる

x=['a','b','c']
y=''.join(x)
z=','.join(x)
print(z)
# .joinで間隔をあけたりできる

x=' 寺下 和樹 '
y=x.strip()
print(y)
x='_2024_4_5_'
y=x.strip('_')
print(y)
x=' a b '
y=x.lstrip()
z=x.rstrip()
print(z)
# lstripはleft左の空文字を削除、rstripはright右の空文字を削除
# stripでxの不必要な部分を削除できる

x='987'
y=x.zfill(10)
print(y)
# id作成の時などに使われる、数字の分の桁になる（上記に場合だとooooooo987）

x='abcdEf'.upper()
y='AbcdEf'.lower()
print(x)
print(y)
# upperはすべて大文字、lowerはすべて小文字



        

