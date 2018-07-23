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
