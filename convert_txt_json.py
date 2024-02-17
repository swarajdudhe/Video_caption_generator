import json

def txt_to_json(txt_data):
    json_data = {}

    lines = txt_data.split('\n')

    for line in lines:
        # Split the line and check if it has at least three elements
        elements = line.split(':')
        if len(elements) >= 3:
            videoId, description, duration = elements[:3]
            json_data[videoId+".avi"] = {
                'description': description
            }
        else :
            videoId, description = elements[:2]
            json_data[videoId] = {
                'description': description
            }

    return json_data

def save_json(data, filename='output.json'):
    with open(filename, 'w') as json_file:
        json.dump(data, json_file, indent=2)

# Read data from the text file
with open('data/testing_data/ground_truth.txt', 'r') as txt_file:
    txt_data = txt_file.read()

# Convert txt data to JSON
json_data = txt_to_json(txt_data)

# Save JSON data to a file
save_json(json_data, 'data/testing_data/ground_result.json')