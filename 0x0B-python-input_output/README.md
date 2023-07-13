			python files and json

	Json.dump() - is used to serialize a Python object and write it directly to a file-like object.
It takes two parameters: the Python object to be serialized and the file-like object where the JSON data will be written.
It directly writes the JSON data to the specified file-like object, without returning any value.

			example:
import json
data = {"name": "John Doe", "age": 25, "city": "New York"}
with open("data.json", "w") as file:
    json.dump(data, file)
In the above example, the data dictionary is serialized into JSON format and written to the file data.json using json.dump()

	json.dumps() - 
