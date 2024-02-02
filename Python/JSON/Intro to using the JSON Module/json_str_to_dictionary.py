import json

a_string = '{"planet":"Earth", "animal":["cat", "dog"], "numbers":{"One":1, "Two":2}}'

change_string_to_dictionary = json.loads(a_string)

print(type(change_string_to_dictionary))
print(change_string_to_dictionary["planet"])
print(change_string_to_dictionary["animal"][0])
print(change_string_to_dictionary["numbers"]["One"])
