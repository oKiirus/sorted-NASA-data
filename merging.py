import csv

data1 = []
data2 = []

with open('data.csv', 'r') as f:
    csvReader = csv.reader(f)
    for i in csvReader: 
        data1.append(i)
with open('sortedData.csv', 'r') as f:
    csvReader = csv.reader(f)
    for i in csvReader: 
        data2.append(i)
headers1 = data1[0]
planetInfo1 = data1[1:]
headers2 = data2[0]
planetInfo2 = data2[1:]
headers = headers1 + headers2
finalData = []

for i, v in enumerate(planetInfo1):
    finalData.append(planetInfo1[i] + planetInfo2[i])

with open('finalData.csv', 'a+') as f:
    csvWriter = csv.writer(f)
    csvWriter.writerow(headers)
    csvWriter.writerows(finalData)
