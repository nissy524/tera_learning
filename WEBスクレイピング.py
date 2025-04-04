from bs4 import BeautifulSoup
import requests

res=requests.get('https://www.orangepage.net/recipes/search/6')
soup=BeautifulSoup(res.text,'html.parser')

h2_tags=soup.find_all('h2')
print([x for x in h2_tags[2].stripped_strings])

from bs4 import BeautifulSoup
#BeautifulSoupはHTMLやXMLの分析のためのライブラリ（bs4は必要なパッケージ）
import requests
res=requests.get('https://www.orangepage.net/recipes/search/6')
soup=BeautifulSoup(res.text,'html.parser')
recipes=soup.find('div',id='recipe_list',class_='recipesList')
p_tit_tags=recipes.find_all('p',class_='tit')
print(x.string for x in p_tit_tags)







