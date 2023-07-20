import interf 
from datetime import datetime
import json


interface = interf.interfRU()

curentDay = datetime.today()
print("%d-%d-%d %d:%d:%d" %(curentDay.day, curentDay.month, curentDay.year, curentDay.hour, curentDay.minute, curentDay.second));

tempTitl = "temptitle"
tempForTest = {"title": tempTitl, "cyrentTime" : str(curentDay), "editTime": str(curentDay), "content": "1234124"}

print(tempForTest)


#with open('data.json', 'a') as f:
 #   json.dump(tempForTest, f, indent='\t')

#with open('data.json') as f:
 #   templates = json.load(f)

f = open('data.json')
json = json.load(f)

for i in json:
    print(i + " : " +json[i])

#date_time_obj = datetime.strptime(templates["cyrentTime"], '%Y-%m-%d %H:%M:%S.%f')

