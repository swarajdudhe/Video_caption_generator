from rouge_score import rouge_scorer
import json
import nltk
nltk.download('punkt')

def read_captions_from_json(file_path):
    with open(file_path, 'r') as file:
        captions_data = json.load(file)
    return captions_data

def calculate_rouge_scores(reference, candidate):
    scorer = rouge_scorer.RougeScorer(['rouge1', 'rouge2', 'rougeL'], use_stemmer=True)
    
    scores = scorer.score(reference, candidate)

    return scores

def calculate_rouge_accuracy(gen_captions_file, ref_captions_file, threshold=0.5):
    gen_captions_data = read_captions_from_json(gen_captions_file)
    ref_captions_data = read_captions_from_json(ref_captions_file)

    total_correct = 0

    for video_name, gen_caption_info in gen_captions_data.items():
        gen_caption = gen_caption_info['description']
        
        if video_name in ref_captions_data:
            ref_captions = ref_captions_data[video_name]['description']
            
            # Calculate ROUGE scores
            rouge_scores = calculate_rouge_scores(ref_captions, gen_caption)

            # Check if ROUGE-L F1 Score meets the threshold
            if rouge_scores['rougeL'].fmeasure >= threshold:
                total_correct += 1

    # Calculate accuracy
    accuracy = total_correct / len(gen_captions_data)
    return accuracy

# Replace 'gen_captions.json' and 'handwritten_captions.json' with the paths to your actual JSON caption files
gen_captions_file_path = 'data/testing_data/result.json'
handwritten_captions_file_path = 'data/testing_data/ground_result.json'

# Calculate overall accuracy using ROUGE scores
accuracy = calculate_rouge_accuracy(gen_captions_file_path, handwritten_captions_file_path)

print(f"Overall ROUGE Accuracy: {accuracy * 100:.2f}%")
