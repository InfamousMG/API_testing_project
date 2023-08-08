import json

"""parsing json from a string pasted into the file"""
courses = '{"name": "Michal", "language": ["Java", "Python"]}'

# Load method parse json and return dictionary
dict_courses = json.loads(courses)
print(dict_courses["name"])

print(dict_courses["language"][0])


for key in dict_courses:
    print(key)
    print(dict_courses[key])

"""parsing json from an external file"""
with open("C:\\Users\\mgos\\Downloads\\pythonBasics\\new.json") as f:
    data = json.load(f)
    print(data)
    print(type(data))


