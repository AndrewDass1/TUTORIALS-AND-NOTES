import json

a_dictionary = {"first_key": 13, "second_key": ["sample_text", 15]}
change_dictionary_to_string = json.dumps(a_dictionary)
print(type(change_dictionary_to_string))
print(change_dictionary_to_string)
