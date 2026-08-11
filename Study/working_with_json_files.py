import json
# loads to load a json file into my file
data = json.loads()
print(data)

# dumps to dump in new data 
new_data = json.dumps()
print(new_data)

# sort-keys for sorting in alphabetic order
new_data = json.dumps(sort_keys=True)

# load to load a json object into python file
with open("name_of_file") as f:
    data = json.load(f)

# dump to convert data to json file
# indent argument to make a file more readable
with open("new_data", "w") as f:
    json.dump(data, f, indent= 2)
