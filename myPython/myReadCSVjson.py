import csv
import json

with open("/Users/jiyoungpark/Downloads/myScripts/myTech/Hyun_python/interview_questions/PoinsettiaTennis2025.csv", newline='') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

x = '{"name":"John", "age": 30, "city":"San Diego"}'
# parse x
y = json.loads(x)
print(y["age"])
z = json.dumps(x)
print(z)