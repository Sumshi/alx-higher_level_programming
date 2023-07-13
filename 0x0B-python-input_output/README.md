			 python files and json

	Json.dump() - is used to serialize a Python object and write it directly to a file-like object.
It takes two parameters: the Python object to be serialized and the file-like object where the JSON data will be written.
It directly writes the JSON data to the specified file-like object, without returning any value.

			example for json.dump():
	import json
	data = {"name": "John Doe", "age": 25, "city": "New York"}
	with open("data.json", "w") as file:
    	json.dump(data, file)
In the above example, the data dictionary is serialized into JSON format and written to the file data.json using json.dump()

	json.dumps() -  is used to serialize a Python object and return the resulting JSON data as a string.
It takes one parameter: the Python object to be serialized.
It returns a string containing the JSON data.

		example for json.dumps():
	import json
	data = {"name": "John Doe", "age": 25, "city": "New York"}
	json_string = json.dumps(data)
	print(json_string)
	print(type(json_string))
	print(type(data))

in the above example, the data dictionary is serialized into JSON format using json.dumps() and then printed to the console.

In summary, the key difference between json.dump() and json.dumps() is that json.dump() directly writes the serialized JSON data to a file-like object, while json.dumps() returns the serialized JSON data as a string.

	json.load() - is used to deserialize JSON data from a file-like object.

It takes one parameter: the file-like object from which to read the JSON data.
It returns a Python object representing the deserialized JSON data.

		example for json.load():
	import json
	with open("data.json", "r") as file:
    	data = json.load(file)
    	print(data)
In the above example, the JSON data from the file data.json is read using json.load() and stored in the data variable as a Python object.


	json.loads() - is used to deserialize JSON data from a string.
It takes one parameter: the string containing the JSON data.
It returns a Python object representing the deserialized JSON data.

		example for json.loads()
	import json
	json_string = '{"name": "John Doe", "age": 25, "city": "New York"}'
	data = json.loads(json_string)
	print(data)
In the above example, the JSON data stored in the json_string variable is deserialized using json.loads() and stored in the data variable as a Python object.

Both json.load() and json.loads() perform the reverse operation of their serialization counterparts (json.dump() and json.dumps()) by converting JSON data into Python objects.

