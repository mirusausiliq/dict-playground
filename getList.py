import os
import json 

input_folder = './dict/^'
output_file = './dict/^/list.json'

json_files = [filename[:-5] for filename in os.listdir(input_folder) if filename.endswith('.json')]
json_files.sort()

with open(output_file, 'w', encoding='utf-8') as file:
  json.dump(json_files, file)
