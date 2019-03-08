# IN4325
This is the repository for team project of IN4325 Information Retrieval.

We will reproduce the paper [Ad Hoc Table Retrieval using Semantic Similarity](https://arxiv.org/pdf/1802.06159.pdf).

## Test collection

The table corpus is [WikiTables](http://websail-fe.cs.northwestern.edu/TabEL/), which comprises 1.6M tables extracted from Wikipedia. A pre-processed version made by the author of the paper is availabel [here](http://iai.group/downloads/smart_table/WP_tables.zip).

The `data/queries.txt` file contains the search queries. Queries #1-#30 queries constitute *Query subset 1 (QS-1)*, queries #31-#60 constitute *Query subset 2 (QS-2)*.

The `data/qrels.txt` file contains the relevance assessments (in TREC qrels format).  
