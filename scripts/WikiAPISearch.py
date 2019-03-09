"""
    search.py

    MediaWiki Action API Code Samples
    Demo of `Search` module: Search for a text or title
    MIT license
"""

import requests
from pdb import set_trace
import json

S = requests.Session()

URL = "https://en.wikipedia.org/w/api.php"


def gothrough_table_list(Data,querynumber,querystring,features):
    
    for table in filter(lambda x: x["queryId"]==str(querynumber),features):
        count = 0
        table["query"]=querystring
        qlen = len((querystring).split(" "))
        table["qlen"]= qlen
        for retrieved in Data['query']['search']: 
            #set_trace()
            count+=1
            if retrieved['title'] == table['pgTitle']:         
                table["yrank"]= count


raw_json=open("tableListMinimized.json").read()
jsonfeatures = json.loads(raw_json)

queries = ["world interest rates table","2008 beijing olympics","fast cars","clothing sizes","phases of the moon","usa population by state","prime ministers of england","ipod models","bittorrent clients","olympus digital slrs","composition of the sun",
"running shoes","fuel consumption","stock quote tables","top grossing movies","nutrition values","state capitals and largest cities in us","professional wrestlers","company income statements","dog breeds","ibanez guitars","used cellphones","world religions","stocks","academy awards","2008 olympic gold medal winners",
"currencies of different countries","science discoveries","pga leaderboard","pain medications","football clubs city","healthy food cost","capitals attractions","diseases mortality","cigarette brands market share","apples market share","healthy food nutritional value","hormones effects","household chemicals strength","lakes altitude","laptops cpu",
"asian countries currency","diseases risks","external drives capacity","baseball teams captain","maryland counties population","countries capital","diseases incidence","eu countries year joined","irish counties area","cereals nutritional value","erp systems price","cats life span","broadway musicals director","infections treatment",
"food type","board games number of players","google products reviews","constellations closest constellation","games age"]
countQueries=0
for i in queries:
    countQueries+=1
    SEARCHPAGE = i
    PARAMS = {
        'action':"query",
        'list':"search",
        'srsearch': SEARCHPAGE,
        'format':"json",
        'srlimit':"200"
    }
    
    R = S.get(url=URL, params=PARAMS)
    Data = R.json()
    print(i)
 
    gothrough_table_list(Data,countQueries,i,jsonfeatures)
file ='FeaturesAndQueries.json'
saveFile = open(file, 'a')
saveFile.write(json.dumps(jsonfeatures))
