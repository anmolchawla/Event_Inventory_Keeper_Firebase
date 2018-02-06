
import csv
import json
from firebase import firebase
from collections import defaultdict
import re
import sys
import yaml



if __name__ == '__main__':  
    user_input_data = sys.argv[1]
       
    
    csvfile = open('./'+user_input_data, 'r')
    

    fieldnames =("id","name","sponsor","event","venue","place","physical_description","ocassion","notes","call_number","keywords","langauge","date","location","location_type","currency","currency_symbol","status","page_count","dish_count")
    reader = csv.DictReader( csvfile, fieldnames)

    num = list(range(0,202))
    j = 0


    jsonfile='{'
    for row in reader:
        jsonfile+=('"%s"' % num[j])
        j += 1
        jsonfile+=(":")
        jsonfile+=json.dumps(row)
        jsonfile+=(',')
        jsonfile+=('\n')
    jsonfile+=('"%s"' % num[j])
    jsonfile+=(":")
    jsonfile+=('{')
    jsonfile+=('"End":"Data"')   
    jsonfile+=('}')
    jsonfile+=('}')
    jsonfile.replace("\\", '')



  #  with open (json_update_path,'w') as json_data:
   #     data = json.load(json_data)
    

    firebase = firebase.FirebaseApplication('https://dmhw1-28e4c.firebaseio.com/')
    pushindata = firebase.put('','menu',json.loads(jsonfile))
    csvfile = open(user_input_data, 'r')
    fieldnames = ("id","name","sponsor","event","venue","place","physical_description","ocassion","notes","call_number","keywords","langauge","date","location","location_type","currency","currency_symbol","status","page_count","dish_count")
    reader = csv.DictReader( csvfile, fieldnames)
    next(reader,None)
    dict = defaultdict(list)

    for row in reader:     
        for word in re.sub("[^\w]", " ", row['event']).split():
                if word.upper() in dict:
                    dict[word.upper()].append(row['id'])
                else :
                    dict[word.upper()]=[row['id']]

  #  jsonfile_update = open(json_update_path, 'w')
    r = (dict)
   

    pushindata = firebase.put('',"menu_update", r)




