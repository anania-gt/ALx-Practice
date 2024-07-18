import json

# Python dictionary
python_dict = {
    "name": "John",
    "age": 30,
    "city": "New York",
    "is_student": False,
    "courses": ["Math", "Science"]
}

# Convert to JSON string
json_string = json.dumps(python_dict)
print(json_string)


#writing to a json file

with open('data.json', 'w') as obj:
    json.dump(json_string,obj)


json_string = json.dumps(python_dict, indent=4)
print(json_string)
