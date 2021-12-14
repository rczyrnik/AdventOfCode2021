import json

def read_json_data(file_name):
	file = open(file_name, 'r')
	raw_lines = file.read()
	file.close()
	return raw_lines


data = read_json_data("20211208_1014.csv")
parsed_data = json.loads(data)
participant_ids = parsed_data["members"].keys()

for id in participant_ids: print(id)