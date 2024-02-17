import os
import shutil

def separate_testing_videos(dataset_folder, testing_id_file, output_folder):
    # Read testing video filenames from testing_id.txt
    with open(testing_id_file, 'r') as file:
        testing_video_ids = file.read().splitlines()

    # Create output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Move testing videos to the output folder
    for video_id in testing_video_ids:
        video_filename = f"{video_id}.avi"  # Assuming video files are in mp4 format
        source_path = os.path.join(dataset_folder, video_filename)
        destination_path = os.path.join(output_folder, video_filename)

        # Move the file
        try:
            shutil.move(source_path, destination_path)
            print(f"Moved {video_filename} to {output_folder}")
        except FileNotFoundError:
            print(f"File {video_filename} not found in {dataset_folder}")

# Example usage
dataset_folder = "data/training_data/video"
testing_id_file = "data/training_data/train_list.txt"
output_folder = "data/training_videos"

separate_testing_videos(dataset_folder, testing_id_file, output_folder)