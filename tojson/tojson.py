import csv
import json

with open('cu.csv') as f:
       reader = csv.DictReader(f)
       rows = list(reader)

with open('cu.json', 'w') as f:
       json.dump(rows, f)