import pandas as pd
import json
import math
 
from pdb import set_trace
 
# read json into a dataframe
features_idf=pd.read_json("FeaturesAndQueries.json",lines=True)
 
# print schema
#print("Schema:\n\n",features_idf.dtypes)
#print("Number of questions,columns=",features_idf.shape)


#TableList_idf=pd.read_json("tableList.json",lines=True)
raw_json=open("tableList.json").read()
TableList_idf = json.loads(raw_json)


from sklearn.feature_extraction.text import CountVectorizer
import re
 
def get_stop_words(stop_file_path):
    """load stop words """
    
    with open(stop_file_path, 'r', encoding="utf-8") as f:
        stopwords = f.readlines()
        stop_set = set(m.strip() for m in stopwords)
        return frozenset(stop_set)
 
queries = ["world interest rates table","2008 beijing olympics","fast cars","clothing sizes","phases of the moon","usa population by state","prime ministers of england","ipod models","bittorrent clients","olympus digital slrs","composition of the sun",
"running shoes","fuel consumption","stock quote tables","top grossing movies","nutrition values","state capitals and largest cities in us","professional wrestlers","company income statements","dog breeds","ibanez guitars","used cellphones","world religions","stocks","academy awards","2008 olympic gold medal winners",
"currencies of different countries","science discoveries","pga leaderboard","pain medications","football clubs city","healthy food cost","capitals attractions","diseases mortality","cigarette brands market share","apples market share","healthy food nutritional value","hormones effects","household chemicals strength","lakes altitude","laptops cpu",
"asian countries currency","diseases risks","external drives capacity","baseball teams captain","maryland counties population","countries capital","diseases incidence","eu countries year joined","irish counties area","cereals nutritional value","erp systems price","cats life span","broadway musicals director","infections treatment",
"food type","board games number of players","google products reviews","constellations closest constellation","games age"]

 
#get the text column
PgTitles = []
SectionTitles = []
TableCaptions = []
TableHeading = []
TableBody = []
Catchall=[]
#docs =[x['data']['pgTitle'] for x in TableList_idf]
tableset= []
ReadTables =[]
for table in TableList_idf:
    if table["id"] not in ReadTables:
        try:
            ReadTables.append(table["id"])
            
            PgTitles.append(table['data']['pgTitle'])
            SectionTitles.append(table['data']['secondTitle'])
            TableCaptions.append(table['data']['caption'])
            heading =""
            for i in table['data']['title']:
                heading = heading+i
            TableHeading.append(heading)
            
            body =""
            for rows in table['data']['data']:
                for column in rows:
                    body = body+column
            TableBody.append(body) 
            Catchall.append(table['data']['pgTitle']+table['data']['secondTitle']+table['data']['caption']+heading+body)

        except:
            set_trace()
numberOfDocuments = len(PgTitles)
print(numberOfDocuments)

def CalculateQueryIDFList(countedlist,numberOfDocs):
    IDFs= []
    try:
        for i in countedlist:
            try:
            #if i != 0:
                IDFs.append(math.log((numberOfDocs - i+0.5)/(i+0.5)))
            
            #else: 
            except:
                IDFs.append(0)
    except:
        set_trace()
    return IDFs   

def CalculateQueryIDF(count,numberOfDocs):
    try:
        IDF=math.log((numberOfDocs - count+0.5)/(count+0.5))
    except:
        IDF=0
    return IDF   


queryCountPgTitles=[]
queryCountSectionTitles=[]
queryCountTableCaptions=[]
queryCountTableHeading=[]
queryCountTableBody=[]
queryCountCatchAll= []

for query in  queries:
    countPgTitlesIDF = 0    
    countSectionTitlesIDF = 0
    countTableCaptionsIDF = 0
    countTableHeadingIDF = 0
    countTableBodyIDF = 0
    countCatchAllIDF = 0
    for term in query.split(" "):
        countPgTitles = 0    
        countSectionTitles = 0
        countTableCaptions = 0
        countTableHeading = 0
        countTableBody = 0
        countCatchAll = 0
        for i in PgTitles:
            if term in i: 
                countPgTitles +=1
               
        for i in SectionTitles:
            if term in i: 
                countSectionTitles +=1
                #set_trace()
        for i in TableCaptions:
            if term in i: 
                countTableCaptions +=1
                #set_trace()
        for i in TableHeading:
            if term in i: 
                countTableHeading +=1
                #set_trace()
        for i in TableBody:
            if term in i: 
                countTableBody +=1
                #set_trace()
        for i in Catchall:
            if term in i: 
                countCatchAll +=1
        countPgTitlesIDF        +=  CalculateQueryIDF(countPgTitles,numberOfDocuments)     
        countSectionTitlesIDF   =   countSectionTitlesIDF   +  CalculateQueryIDF(countSectionTitles,numberOfDocuments)
        countTableCaptionsIDF   =   countTableCaptionsIDF   +  CalculateQueryIDF(countTableCaptions,numberOfDocuments)
        countTableHeadingIDF    =   countTableHeadingIDF    +  CalculateQueryIDF(countTableHeading,numberOfDocuments)
        countTableBodyIDF       =   countTableBodyIDF       +  CalculateQueryIDF(countTableBody,numberOfDocuments)
        countCatchAllIDF        =   countCatchAllIDF        +  CalculateQueryIDF(countCatchAll,numberOfDocuments)
        #set_trace()
        #print( countPgTitlesIDF      )
        #print( countSectionTitlesIDF )
        #print( countTableCaptionsIDF )
        #print( countTableHeadingIDF  )
        #print( countTableBodyIDF     )
        #print( countCatchAllIDF      )

    queryCountPgTitles.append(countPgTitlesIDF)   
    queryCountSectionTitles.append(countSectionTitlesIDF)
    queryCountTableCaptions.append(countTableCaptionsIDF)
    queryCountTableHeading.append(countTableHeadingIDF)
    queryCountTableBody.append(countTableBodyIDF)
    queryCountCatchAll.append(countCatchAllIDF)



raw_json=open("FeaturesAndQueries.json").read()
jsondata = json.loads(raw_json)
count =0
for query in queries:
    count+=1
    #set_trace()
    for j in filter(lambda x: x["queryId"]==str(count),jsondata):
    #for j in jsondata:
        #if j["queryId"]==count:
            #set_trace()
        j["IDFpageTitle"]= queryCountPgTitles[count-1]
        j["IDFsectionTitle"]= queryCountSectionTitles[count-1]
        j["IDFtableCaption"]= queryCountTableCaptions[count-1]
        j["IDFtableHeading"]= queryCountTableHeading[count-1]
        j["IDFtableBody"]= queryCountTableBody[count-1]
        j["IDFCatchAll"]= queryCountCatchAll[count-1]

saveFile = open('FeaturesAndQuerieswIDF.json', 'a')
saveFile.write(json.dumps(jsondata))  

#bla = list(filter(lambda x :queries[1]in x,docs))



