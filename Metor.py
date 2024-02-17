from nltk.translate.meteor_score import meteor_score
from nltk.tokenize import word_tokenize
import json
import nltk

nltk.download('punkt')
nltk.download('wordnet')

def read_captions_from_json(file_path):
    with open(file_path, 'r') as file:
        captions_data = json.load(file)
    return captions_data

def calculate_meteor_accuracy(gen_captions_data, ref_captions_data, threshold=0.5):
    total_correct = 0

    for video_name, gen_caption_info in gen_captions_data.items():
        gen_caption = gen_caption_info['description']

        if video_name in ref_captions_data:
            ref_captions = ref_captions_data[video_name]['description']

            # Tokenize the captions
            gen_tokenized = word_tokenize(gen_caption.lower())
            ref_tokenized = word_tokenize(ref_captions.lower())

            # Calculate METEOR score
            meteor_score_value = meteor_score([ref_tokenized], gen_tokenized)

            # Check if METEOR score meets the threshold
            if meteor_score_value >= threshold:
                total_correct += 1

    # Calculate accuracy
    accuracy = total_correct / len(gen_captions_data)
    return accuracy

# Replace 'gen_captions.json' and 'handwritten_captions.json' with the paths to your actual JSON caption files
gen_captions_file_path = 'data/testing_data/result.json'
handwritten_captions_file_path = 'data/testing_data/ground_result.json'

# Load captions from JSON files
gen_captions_data = read_captions_from_json(gen_captions_file_path)
handwritten_captions_data = read_captions_from_json(handwritten_captions_file_path)

# Calculate overall METEOR accuracy
accuracy = calculate_meteor_accuracy(gen_captions_data, handwritten_captions_data)

print(f"Overall METEOR Accuracy: {accuracy * 100:.2f}%")
