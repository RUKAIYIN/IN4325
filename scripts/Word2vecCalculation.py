import gensim
from pdb import set_trace
import logging 
import json

raw_json=open("tableWords.json").read()
tables  = json.loads(raw_json)

# Load Google's pre-trained Word2Vec model.
model = gensim.models.KeyedVectors.load_word2vec_format('GoogleNews-vectors-negative300.bin', binary=True)  

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)


for query in tables:
    query["vectors"]=[]
    for word in query["words"]:
        try:
            vector = model.get_vector(word)
            #set_trace()
            query["vectors"].append({word:[a.item() for a in vector]})
        except:
             query["vectors"].append({word:"not available"})
        

saveFile = open('tableVectors.json', 'a')
saveFile.write(json.dumps(tables))  



