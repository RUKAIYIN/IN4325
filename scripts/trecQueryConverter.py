# This script creates trec query file format for each query
# author: Nick Boyd
#
# <TOP>
# <NUM>Query#</NUM>
# <TITLE>Query string</TITle>
# </TOP>

#List of queries from queries.txt
queries = ["world interest rates table","2008 beijing olympics","fast cars","clothing sizes","phases of the moon","usa population by state","prime ministers of england","ipod models","bittorrent clients","olympus digital slrs","composition of the sun",
"running shoes","fuel consumption","stock quote tables","top grossing movies","nutrition values","state capitals and largest cities in us","professional wrestlers","company income statements","dog breeds","ibanez guitars","used cellphones","world religions","stocks","academy awards","2008 olympic gold medal winners",
"currencies of different countries","science discoveries","pga leaderboard","pain medications","football clubs city","healthy food cost","capitals attractions","diseases mortality","cigarette brands market share","apples market share","healthy food nutritional value","hormones effects","household chemicals strength","lakes altitude","laptops cpu",
"asian countries currency","diseases risks","external drives capacity","baseball teams captain","maryland counties population","countries capital","diseases incidence","eu countries year joined","irish counties area","cereals nutritional value","erp systems price","cats life span","broadway musicals director","infections treatment",
"food type","board games number of players","google products reviews","constellations closest constellation","games age"]

def write_queries():
	#output file
	with open('../data/queries.trec', 'w') as f:
		count=1
		for query in queries:
	 		print >> f, '<TOP>\n<NUM>' + str(count) + '</NUM>\n<TITLE>' + query + '</TITLE>\n</TOP>'
			count = count + 1

#run it
write_queries()
