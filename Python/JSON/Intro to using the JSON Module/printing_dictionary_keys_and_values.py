import json

a_string = '{"planet":"Earth", "animal":["cat", "dog"], "numbers":{"One":1, "Two":2}}'

change_string_to_dictionary = json.loads(a_string)

for key in change_string_to_dictionary:
	print(key) #Prints all keys
  print(change_string_to_dictionary[key]) #Prints all values
