import re
s='090333'
m=re.match(r'[0-9]{3}',s)
print(m)
if m:
    print(m.group())
    print(m.span())
    
import re
s='bananaは￥300です'
m=re.search(r'[￥[1-9][0-9]*',s)
print(m)
if m:
    print(m.group())
    print(m.span())

import re

s='この洋服は$100です'
m=re.search(r'\$[0-9]+',s)
#正規表現で記号として使う文字をそのまま文字として使う場合エスケープをする（\,/　etc..)
print(m)
if m:
    print(m.group())
    print(m.span())
