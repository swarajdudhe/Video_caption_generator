import json

def convert_json_structure(input_file, output_file):
    """Converts a JSON file structure to a list of dicts with caption and id keys."""

    with open(input_file, 'r') as f:
        data = json.load(f)

    output_data = []
    for video_id, description in data.items():
        output_data.append({"caption": description["description"], "id": video_id})

    with open(output_file, 'w') as f:
        json.dump(output_data, f, indent=4)  # Indent for readability

if __name__ == "__main__":
    input_file = 'data/testing_data/ground_truth.json'  # Replace with your input file path
    output_file = 'data/testing_data/ground_output.json'  # Replace with your desired output file path
    convert_json_structure(input_file, output_file)
