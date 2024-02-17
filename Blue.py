from nltk.translate.bleu_score import sentence_bleu, corpus_bleu
from nltk.tokenize import word_tokenize
import json
import nltk
nltk.download('punkt')

def read_captions_from_json(file_path):
    with open(file_path, 'r') as file:
        captions_data = json.load(file)
    return captions_data

def calculate_accuracy(gen_captions_file, ref_captions_file, threshold=0.5):
    gen_captions_data = read_captions_from_json(gen_captions_file)
    ref_captions_data = read_captions_from_json(ref_captions_file)

    total_correct = 0

    for video_name, gen_caption_info in gen_captions_data.items():
        gen_caption = gen_caption_info['description']
        
        if video_name in ref_captions_data:
            ref_captions = ref_captions_data[video_name]['description']
            
            gen_tokenized = word_tokenize(gen_caption.lower())
            ref_tokenized = word_tokenize(ref_captions.lower())

            # Calculate BLEU score
            bleu_score = sentence_bleu([ref_tokenized], gen_tokenized)

            # Check if BLEU score meets the threshold
            if bleu_score >= threshold:
                total_correct += 1

    # Calculate accuracy
    accuracy = total_correct / len(gen_captions_data)
    return accuracy

# Replace 'gen_captions.json' and 'handwritten_captions.json' with the paths to your actual JSON caption files
gen_captions_file_path = 'data/testing_data/result.json'
handwritten_captions_file_path = 'data/testing_data/ground_result.json'

# Calculate overall accuracy
accuracy = calculate_accuracy(gen_captions_file_path, handwritten_captions_file_path)

print(f"Overall Accuracy: {accuracy * 100:.2f}%")
#METEOR, ROUGE, and CIDEr,