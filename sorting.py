import csv

data = []
with open('data2.csv', 'r') as f:
    csvReader = csv.reader(f)
    for i in csvReader: 
        data.append(i)
headers = data[0]
planetInfo = data[1:]
for i in planetInfo:
    i[0] = i[0].lower()

planetInfo.sort(key = lambda planetInfo : planetInfo[0])

with open('sortedData.csv', 'a+') as f:
    csvWriter = csv.writer(f)
    csvWriter.writerow(headers)
    csvWriter.writerows(planetInfo)
    

