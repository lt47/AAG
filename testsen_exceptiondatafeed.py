import csv, json

with open('senate_exceptiondatafeed.csv', 'rb') as csvdata:
    next(csvdata, None) # skip the headers
    reader = csv.DictReader(csvdata,fieldnames=['datetime', 'name','rule'])
    json.dump([row for row in reader], open('testsen_exceptiondatafeed.json', 'w+'))
