
import json
import math
 
from pdb import set_trace

raw_json=open("tableWords.json").read()
tables  = json.loads(raw_json)

#start by going through all tables, combining terms to make counting easier 
tableTerms =[]
for table in tables:
    table["terms combined"]=''
    terms =''
    table["termValues"]={}
    for word in table["words"]:
        terms=terms +' '+word 
        table["termValues"][word] = {'TF':"x",'IDF':"x",'TFIDF':"x"}
    tableTerms.append(terms)
    table["terms combined"]=terms

    #Here we go through the words again and calculate the TF
    for word in table["words"]:
        occurances =table["terms combined"].count(word)
        numberofTerms= len(table["terms combined"].split(" "))      
        TF =occurances/numberofTerms
        table["termValues"][word]["TF"]=TF


#We need to have each table only once so we dont recount the same occurance.
NoDuplicates=[]
ReadTables = []
for table in tables:
    if table["id"] not in ReadTables:
        ReadTables.append(table["id"])
        NoDuplicates.append(table["terms combined"])
NumberOfTables =len(ReadTables)


#Now we can Calculatee the IDFs for each term

for table in tables:
    for word in table["words"]:
        countDocuments=0
        for i in NoDuplicates:
            if word in i:
                countDocuments +=1
        IDF = math.log(NumberOfTables/countDocuments)
   
        table["termValues"][word]["IDF"]=IDF
        table["termValues"][word]["TFIDF"]=IDF*table["termValues"][word]["TF"]

saveFile = open('tableWordsTFIDF.json', 'a')
saveFile.write(json.dumps(tables))  




raw_json=open("queryWords.json").read()
queries  = json.loads(raw_json)

#start by going through all queries, combining terms to make counting easier 
queryTerms =[]
for query in queries:
    query["terms combined"]=''
    terms =''
    query["termValues"]={}
    for word in query["words"]:
        terms=terms +' '+word 
        query["termValues"][word] = {'TF':"x",'IDF':"x",'TFIDF':"x"}
    queryTerms.append(terms)
    query["terms combined"]=terms

    #Here we go through the words again and calculate the TF
    for word in query["words"]:
        occurances =query["terms combined"].count(word)
        numberofTerms= len(query["terms combined"].split(" "))      
        TF =occurances/numberofTerms
        query["termValues"][word]["TF"]=TF

for query in queries:
    for word in query["words"]:
        countDocuments=0
        for i in NoDuplicates:
            if word in i:
                countDocuments +=1
        try:
            IDF = math.log(NumberOfTables/countDocuments)
        except:
            IDF= 0

        query["termValues"][word]["IDF"]=IDF
        query["termValues"][word]["TFIDF"]=IDF*query["termValues"][word]["TF"]


saveFile = open('queryWordsTFIDF.json', 'a')
saveFile.write(json.dumps(queries)) 
   







