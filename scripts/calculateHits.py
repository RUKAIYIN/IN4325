import json
from pdb import set_trace
import csv

raw_json=open("FeaturesAndQuerieswIDF.json").read()
FeaturesJSON = json.loads(raw_json)

raw_json=open("tableList.json").read()
TableJSON = json.loads(raw_json)

'''
def read_qrels():
    #set_trace()
    qrelTableList=[] 
    with open('.\www2018-table\data\qrels.txt') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter='\t')
        line_count = 0
        for row in csv_reader:   
            qrelTableList.append([row[0],row[2],row[3]]) 
            line_count += 1
    #set_trace()
    return qrelTableList

qrelslist = read_qrels()

for  line in FeaturesJSON:
    for table in qrelslist:
        if ((table[1]==line["id"])&(table[0]==line["queryId"])):
            line["RelevanceJudgement"]=table[2]
''' 





for  line in FeaturesJSON:
    #set_trace()
    
    for table in filter(lambda x :x["id"]==line["id"],TableJSON):
        body =""
        leftMost = ""
        secondLeftMost=""
        pgTitle =table["data"]["pgTitle"]
        tableCaption = table["data"]["caption"]
        for rows in table['data']['data']:
            countrow =0
            for column in rows:
                body = body+column
                countrow+=1
            leftMost+=rows[0]
            if countrow>1:
                secondLeftMost+=rows[1]

   

    bodyhits = 0
    leftHits=0
    secondLeftHits = 0
    pgTitlehits =0
    tableCaptionHits = 0
    for term in (line["query"]).split(" "):
        bodyhits += body.count(term) 
        leftHits +=leftMost.count(term)
        secondLeftHits += secondLeftMost.count(term)
        pgTitlehits+= pgTitle.count(term)
        tableCaptionHits+=tableCaption.count(term)


    
    #print(leftHits)
    #print(secondLeftHits)
    #print(bodyhits)

    line["hitsLC"]=leftHits
    line["hitsSLC"]=secondLeftHits
    line["hitsB"]=leftHits
    line["hitsPageTitile"]=pgTitlehits
    line["hitsTableCaption"]=tableCaptionHits





saveFile = open('final.json', 'a')
saveFile.write(json.dumps(FeaturesJSON))  
    