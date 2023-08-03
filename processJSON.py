import os
import re
import json 
import getIPA

def process_json(input_path, output_path):
    with open(input_path, 'r', encoding='utf-8') as file:
        data = json.load(file)

    # Create the new data structure based on the template
    new_data = {
        "term": data.get("t", ""),
        "properties": {
            "id": "",
            "tags": [],
            "level": {
                "cefr": "",
                "ilrdf": ""
            },
            "basic": {
                "language": "Amis (Pangcah)",
                "language_code": "ami",
                "dialect": "uncertain",
                "origin": "Amis Moedict",
                "author_dictionary": "Safulo Kacaw Lalanges Hakasi",
                "author_datasystem": "Mirusa Usiliq",
                "date": "2023/08/04",
                "time": "00:00",
                "location": "Hualien, Taiwan",
                "device": "MacOS",
                "license": "MIT",
                "reference": "..."
            }
        },
        "linguistics": {
          "pos": "",
          "ipa": getIPA.getIPA(data.get("t", ""))
        },
        "nyms": {
          "synonyms": [],
          "antonyms": [],
          "hyponyms": [],
          "metonyms": [],
          "homonyms": [],
          "heternyms": [],
          "homographs": [],
          "polysemous": [],
          "synecdoche": [],
          "word_family": []
        },
        "definitions": [],
        "declensions": [],
        "conjugation": []
    }

    # Process the definitions and translations
    for item in data.get("h", []):  # Set default empty list if "h" is missing
        for entry in item.get("d", []):  # Set default empty list if "d" is missing
            definition = {
                "language": "zh-tw",
                "explaination": entry.get("f", ""),
                "example": entry.get("e", [""])[0] if entry.get("e") else "",
                "synonyms": entry.get("s", [""])[0] if entry.get("s") else "",
                "usage": "",
                "tips": ""
            }
            new_data["definitions"].append(definition)

    # Write the new data to the output file
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(new_data, f, ensure_ascii=False, indent=2)

# Replace '../docs/p' and './dict' with the actual paths to your folders
input_folder = './amis-moedict/s' # DONT USE
output_folder = './dict/^' 

# Process each JSON file in the input folder
for filename in os.listdir(input_folder):
    if filename.endswith('.json') and filename.startswith('^'):
        input_file = os.path.join(input_folder, filename)
        output_file = os.path.join(output_folder, filename)
        process_json(input_file, output_file)
