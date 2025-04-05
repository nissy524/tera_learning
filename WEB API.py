import requests
res=requests.get('https://zipcloud.ibsnet.co.jp/api/search',params={'zipcode':'2110041'})
# search?zipcode=2110041と同じ使い方　=params
print(res.status_code)
print(res.text)

import requests
res=requests.get('https://zipcloud.ibsnet.co.jp/api/search?zipcode=2110041')
res_json=res.json()
results=res_json['results'][0]
address=results['address1']+results['address2']+results['address3']
print(address)

#APIによって申請を送らないといけないのもある。例は下記
import requests
res=requests.get('https://zipcloud.ibsnet.co.jp/api/search',
                  headers={'Authorization':'xxxxx'})
# xxxxxは取得したキーのこと？

#駅スパートAPI, open Weather Map API,Vision API(有料）,Translation,ケンオールAPI（有料）
# Exchange Rates API(有料)、ALPHA VANTAGE(株)






#res.status_code:200=ok,400=bad request,500=server error
