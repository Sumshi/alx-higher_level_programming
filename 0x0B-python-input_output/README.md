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
