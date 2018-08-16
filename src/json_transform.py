#!/usr/bin/env python
import json
import types

with open('topic.json', 'r', encoding = "utf-8") as load_f:
    load_list = json.loads(load_f.read())

print(type(load_list))

for temp_dict in load_list:
   temp_dict.pop("imageUrl")
   temp_dict.pop("intro")
   temp_dict["topic_name"]=temp_dict["name"]
   temp_dict.pop("name")
   print('val=%s'% (temp_dict))

with open('topic_update.json', 'w', encoding = "utf-8") as f:
    json.dump(load_list, f, ensure_ascii = False)
    
    
    
    
    
    
    
import json
import requests
from urllib import parse
from urllib.parse import quote

with open('topic.json', 'r', encoding = "utf-8") as load_f:
    load_list = json.loads(load_f.read())

jsonList=[]

file_write_obj = open("dest.json", 'w',encoding = "utf-8")

count=64

for temp_dict in load_list:
   temp_dict.pop("imageUrl")
   temp_dict.pop("intro")
   temp_dict["category"]="board"
   temp_dict["bus_id"]=temp_dict["id"]
   temp_dict["id"]=count
   temp_dict["topic_name"]=temp_dict["name"]
   temp_dict.pop("name")
   jsonList.append(str(temp_dict))
   print(json.dumps(temp_dict,ensure_ascii=False))
   file_write_obj.writelines(json.dumps(temp_dict,ensure_ascii=False))
   file_write_obj.write('\n')
   count=count+1
