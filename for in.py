names=('斎藤','寺下','鈴木')
x=[i+'さん' for i in names]
print(x)

x=[i for i in range(11)if i%2!=0]
print(x)

foods=['apple','banana','lemon']
x=[i for i in foods if 'a'in i]
print(x)

Kanto=['千葉','栃木','東京','埼玉','茨城','群馬','神奈川']
x=[i+'都' if i =='東京' else i +'県' for i in Kanto]
print(x)
#  i for i in ~ 'i'の部分忘れがち




