import json

# This script creates trec document format for each table
# author: Nick Boyd
#
# <DOC>
# <DOCNO>table id</DOCNO>
# Content of the table. (titles, captions, heading, body)
# </DOC>
# <DOC>

#Read in json file
raw_json=open("../data/tableList.json").read()
TablesJSON=json.loads(raw_json)

#Keep track of tables added to avoid duplicate tables in file.
tablesAdded=[]

def write_tables():
	with open('../data/tableList.trec', 'w') as f:
		output=''
		for table in TablesJSON:
			#Extract fields from json
			tableId=table["id"]
			pgTitle=table["data"]["pgTitle"]
			secondTitle = table["data"]["secondTitle"]
			caption=table["data"]["caption"]
			title=table["data"]["title"]

			output=pgTitle+'\n'+secondTitle+'\n'+caption + '\n'
			#heading (column keys of table) is a list
			for heading in title:
				output = output + heading
			#loop through body of table
			for rows in table["data"]["data"]:
				body=''
				for column in rows:
        				body=body+column
				output = output + body

			#logic to avoid duplicate tables
			if tableId not in tablesAdded:
				print >> f, '<DOC>\n<DOCNO>' + tableId.encode('utf-8') + '</DOCNO>\n' + output.encode('utf-8') + '\n</DOC>'
			tablesAdded.append(tableId)

#run it
write_tables()
