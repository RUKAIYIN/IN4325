import json
import os
from pdb import set_trace
import csv
import pandas
import pandas as pd



def read_qrels():
    qrelTableList=[] 
    with open('.\www2018-table\data\qrels.txt') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter='\t')
        line_count = 0
        for row in csv_reader:   
            qrelTableList.append([row[0],row[2],row[3]]) 
            line_count += 1
    return qrelTableList


def read_original_json_files(qrelsTableList):
  TableList = []
  ## all the table files from the table corpus need tp be in the following directory
  dir = './tables_redi2_1/'
  files = os.listdir(dir)
  count =0
  countFile = 0
  for file in files:
    countFile +=1
    print("countFile " +str(countFile))
    raw_json=open(dir + '/' + file).read()
    jsondata = json.loads(raw_json)
    for i in jsondata.keys(): #all keys
        #print(i)
        for j in filter(lambda x: x[1]==i,qrelsTableList):
        
            TableList.append({'id':i,'query':j[0], "RelevanceJudgement":j[2],'data': jsondata[i]})
            count +=1
            print(count)
   
  saveFile = open('tableList.json', 'a')
  saveFile.write(json.dumps(TableList))
  return TableList

def read_table_list():
    raw_json=open("tableList.json").read()
    jsondata = json.loads(raw_json)
   
    tableFeatures=[]
    for table in jsondata: #all keys
    
        countNull=0
        for i in table["data"]["data"]: 
            for ii in i:
                if ii =="" :
                     countNull+=1
        tableFeatures.append({'queryId':table["query"],'query':"",'id':table["id"] ,'pgTitle':table["data"]["pgTitle"],'rows': table["data"]["numDataRows"],'cols': table["data"]["numCols"],'numberOfNullsInTable': countNull,'yrank':"0",'relevanceJudgment':table["RelevanceJudgement"]})
        print(table["id"])
    saveFile = open('tableListMinimized.json', 'a')
    saveFile.write(json.dumps(tableFeatures))  

def write_to_csv():
  raw_json=open("final.json").read()
  jsondata = json.loads(raw_json)
  queryIds=[]
  queries = []
  ids = []
  pgTitles = []
  rows = []
  cols = []
  qlens=[]
  numberofNulls = []
  yranks = []
  IDFpageTitles=[]
  IDFsectionTitle=[]
  IDFtableCaption=[]
  IDFtableHeading=[]
  IDFtableBody=[]
  IDFCatchAll=[]
  hitsLCs=[]
  hitsSLCs=[]
  hitsBs=[]
  hitsPageTitles=[]
  hitsTableCaptions=[]
  relevance=[]


  for table in jsondata:
    queryIds.append(table["queryId"])
    queries.append(table["query"])
    ids.append(table["id"])
    pgTitles.append(table["pgTitle"])
    rows.append(table["rows"])
    cols.append(table["cols"])
    numberofNulls.append(table["numberOfNullsInTable"])
    yranks.append(table["yrank"])
    qlens.append(table["qlen"])
    IDFpageTitles.append(table["IDFpageTitle"])
    IDFsectionTitle.append(table["IDFsectionTitle"])
    IDFtableCaption.append(table["IDFtableCaption"])
    IDFtableHeading.append(table["IDFtableHeading"])
    IDFtableBody.append(table["IDFtableBody"])
    IDFCatchAll.append(table["IDFCatchAll"])
    hitsLCs.append(table["hitsLC"])
    hitsSLCs.append(table["hitsSLC"])
    hitsBs.append(table["hitsB"])
    hitsPageTitles.append(table["hitsPageTitile"])
    hitsTableCaptions.append(table["hitsTableCaption"])
    relevance.append(table["relevanceJudgment"])


  df = pandas.DataFrame(data={"QueryID": queryIds, "QueryString": queries,"Table id":ids, "pgTitle":pgTitles,"rows":rows, "cols":cols,"numberofNullsInTable":numberofNulls,"yrank":yranks,"qlen":qlens,"IDFpageTitles":IDFpageTitles,"IDFsectionTitle":IDFsectionTitle,"IDFtableCaption":IDFtableCaption,"IDFtableHeading":IDFtableHeading,"IDFtableBody":IDFtableBody,"IDFCatchAll":IDFCatchAll, "hitsLC": hitsLCs,"hitsSLC": hitsSLCs,"hitsB": hitsBs,"hitsPageTitle": hitsPageTitles,"hitsTableCaption": hitsTableCaptions,"relevanceJudgment":relevance})
  df.to_csv("./FeaturesFinal.csv", sep=',',index=False)

def countQueryLength():
  raw_json=open("FeaturesAndQuerieswIDF.json").read()
  jsondata = json.loads(raw_json)
  for table in jsondata:
    qlen = len((table["query"]).split(" "))
    table["qlen"]= qlen
  file ='FeaturesFinal.json'
  saveFile = open(file, 'a')
  saveFile.write(json.dumps(jsondata))

def go_through_data(session):
  #set_trace()
  session_data = session['data']


if __name__ == "__main__":
    #to read the qrels from origina; qrels file
    qrelsTableList = read_qrels() 

    #Go through Whole table corpus and only extract the tables that are relevant for us. this outputs the 'tableList.json' file.
    read_original_json_files(qrelsTableList)
    
    #Extract information from the tableList that is actually relevant for us. To make the json file smaller. The output file is : 'tableListMinimized.json'
    read_table_list()

    #now the WikiAPISearch python script should be run. It works on the 'tableListMinimized.json' file, it adds te query string, qlen and y rank to the list. and outputs 'FeaturesAndQueries.json'

    #now the QueryIDF file should be run. It works on 'FeaturesAndQueries.json', calculates the query IDFs and outputs 'FeaturesAndQuerieswIDF.json

    #now the calculateHits.py should be run, it works on 'FeaturesAndQuerieswIDF.json' and   'tableList.json' and creates "final.json".

    #when all of the former is done you need to uncomment the line below, and comment out the ones above to write the "final.json" to  csv.
    #the csv  file comes out unsorted but can easily be sorted by the queryid to make it more readable.
    #write_to_csv()
    
  