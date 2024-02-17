from pycocoevalcap.cider.cider import Cider
import json

def read_captions_from_json(file_path):
    with open(file_path, 'r') as file:
        captions_data = json.load(file)
    return captions_data

def calculate_cider_accuracy(gen_captions_file, ref_captions_file):
    gen_captions_data = read_captions_from_json(gen_captions_file)
    ref_captions_data = read_captions_from_json(ref_captions_file)

    cider_scorer = Cider()

    hypothesis = {}
    references = {}

    for video_name, gen_caption_info in gen_captions_data.items():
        gen_caption = gen_caption_info['description']
        
        if video_name in ref_captions_data:
            ref_captions = ref_captions_data[video_name]['description']

            hypothesis[video_name] = [gen_caption]
            references[video_name] = [ref_captions]

    # Compute CIDEr score
    cider_score, _ = cider_scorer.compute_score(references, hypothesis)

    return cider_score

# Replace 'gen_captions.json' and 'handwritten_captions.json' with the paths to your actual JSON caption files
gen_captions_file_path = 'data/testing_data/result.json'
handwritten_captions_file_path = 'data/testing_data/ground_result.json'

# Calculate CIDEr accuracy
cider_accuracy = calculate_cider_accuracy(gen_captions_file_path, handwritten_captions_file_path)

print(f"CIDEr Accuracy: {cider_accuracy}")
