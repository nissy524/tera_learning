x=0
while x<=10:
    x+=1
    print(x)
    if x % 5==0:
        continue
    print('whileの最終行')

with open('aaaaa.txt')as f:
    t=f.readline()
    while t !='':
        print(t)
        t=f.readline()


with open('aaaaa.txt')as f:
    while(t:=f.readline())!='':
        print(t)

import re
s='この金額は1200円です'
if (m:=re.search(r'[0-9]+円',s)):
    print(m.group())
#なんで上記の１２００だけ反映しない？
#whileとfor文はcontinue,break使える、ファイル読むこむ時にwhile


