import string
import csv

csvFile="../data/MultiField/BM25F_20.csv"
file = open("../data/MultiField/BM25F_20.txt", "r")
fileOUT = open("../data/MultiField/BM25F_20_FINAL.txt", "w")
csvOut = open(csvFile, "w")
w = csv.writer(csvOut)

for line in file.readlines():
   list = line.split(' ')
   old = list[3]
   list[3] = str(int(list[3]) + 1)
   list[5] = ''.join(list[5].replace('"',''))[:-1]
   w.writerow(list)
   for value in list:
	   fileOUT.write(value + ' ')
   fileOUT.write('\n')
