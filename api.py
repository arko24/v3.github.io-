import subprocess
import json
import requests as rq
import time, sys, datetime, os, click


#script 
subprocess.call("clear", shell=True)

#class
def xharga(coin):
  url = 'https://api.binance.com/api/v3/ticker/24hr'
  r = rq.get(url)
  js = json.loads(r.text)
  return js

#parameter
bd = xharga('')
crn = ('BUSD')

#tampil
print(bd[501]['symbol'])
print(bd[502]['symbol'])
print(bd[503]['symbol'])
print(bd[504]['symbol'])
print(bd[505]['symbol'])
print(bd[506]['symbol'])
print(bd[507]['symbol'])
print(bd[508]['symbol'])
print(bd[509]['symbol'])
print(bd[510]['symbol'])
print(bd[511]['symbol'])
print(bd[512]['symbol'])
print(bd[513]['symbol'])
print(bd[514]['symbol'])
print(bd[515]['symbol'])
print(bd[516]['symbol'])
print(bd[517]['symbol'])
print(bd[518]['symbol'])
print(bd[519]['symbol'])
print(bd[520]['symbol'])
print(bd[521]['symbol'])
print(bd[522]['symbol'])
print(bd[523]['symbol'])
print(bd[524]['symbol'])
print(bd[525]['symbol'])
print(bd[526]['symbol'])
print(bd[527]['symbol'])
print(bd[528]['symbol'])
print(bd[529]['symbol'])
print(bd[530]['symbol'])
print(bd[531]['symbol'])
print(bd[532]['symbol'])
print(bd[533]['symbol'])
print(bd[534]['symbol'])
print(bd[535]['symbol'])
print(bd[536]['symbol'])
print(bd[537]['symbol'])
print(bd[538]['symbol'])
print(bd[539]['symbol'])
print(bd[540]['symbol'])
print(bd[541]['symbol'])
print(bd[542]['symbol'])
print(bd[543]['symbol'])
print(bd[544]['symbol'])
print(bd[545]['symbol'])
print(bd[546]['symbol'])
print(bd[547]['symbol'])
print(bd[548]['symbol'])
print(bd[549]['symbol'])
print(bd[550]['symbol'])
print(bd[551]['symbol'])
print(bd[552]['symbol'])
print(bd[553]['symbol'])
print(bd[554]['symbol'])
print(bd[555]['symbol'])
print(bd[556]['symbol'])
print(bd[557]['symbol'])
print(bd[558]['symbol'])
print(bd[559]['symbol'])
print(bd[560]['symbol'])
print(bd[561]['symbol'])
print(bd[562]['symbol'])
print(bd[563]['symbol'])
print(bd[564]['symbol'])
print(bd[565]['symbol'])
print(bd[566]['symbol'])
print(bd[567]['symbol'])
print(bd[568]['symbol'])
print(bd[569]['symbol'])
print(bd[570]['symbol'])
print(bd[571]['symbol'])
print(bd[572]['symbol'])
print(bd[573]['symbol'])
print(bd[574]['symbol'])
print(bd[575]['symbol'])
print(bd[576]['symbol'])
print(bd[577]['symbol'])
print(bd[578]['symbol'])
print(bd[579]['symbol'])
print(bd[580]['symbol'])
print(bd[581]['symbol'])
print(bd[582]['symbol'])
print(bd[583]['symbol'])
print(bd[584]['symbol'])
print(bd[585]['symbol'])
print(bd[586]['symbol'])
print(bd[587]['symbol'])
print(bd[588]['symbol'])
print(bd[589]['symbol'])
print(bd[590]['symbol'])
print(bd[591]['symbol'])
print(bd[592]['symbol'])
print(bd[593]['symbol'])
print(bd[594]['symbol'])
print(bd[595]['symbol'])
print(bd[596]['symbol'])
print(bd[597]['symbol'])
print(bd[598]['symbol'])
print(bd[599]['symbol'])
print(bd[600]['symbol'])


