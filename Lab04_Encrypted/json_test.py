import json

# json library: https://docs.python.org/3.5/library/json.html

person = {
    'name': 'Tommy Trojan',
    'email': 'tommy@usc.edu',
    'phone': '213-740-2311',
    'nicknames': [
        'Tommy T',
        'Spirit of Troy',
    ],
}

print(type(person))
print(person)

# TODO: Pretty printing

person_json = json.dumps(person, sort_keys = True, indent = 4)
print (type(person_json))

# TODO: What type is person_json?

print(person_json)

