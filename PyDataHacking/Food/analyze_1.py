import csv
def sortKey(item):
  return int(item[1])

# Process data in datafile
f = open('food.csv')
data = []
# Extract Id, Zip and violations per row
print("Data reduction ...")
for row in csv.DictReader(f):
  data.append((row['Inspection ID'], row['Zip'], row['Violations'].split('|')))
f.close()

print("Analyzing ...")
cviol = {}
for drow in data:
  zipCode = drow[1]
  for viol in drow[2]:
    if viol != '':
      idx = viol[:viol.find(' - Comm')].strip()
      if idx in cviol:
        cviol[idx] += 1
      else:
        cviol[idx] = 1

print("Sorting data ...")
# Prepare a sorted list by most-frequest violation
mySortedList = sorted([ (key, cviol[key]) for key in cviol.keys() ], key=sortKey,reverse=True)
for row in mySortedList:
  print("%-138s %10d" % (row[0], row[1]))
