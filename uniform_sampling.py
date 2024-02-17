import cv2
import os

def uniform_sampling(video_path, output_folder, frame_interval=5):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    cap = cv2.VideoCapture(video_path)
    frame_count = 0

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        if frame_count % frame_interval == 0:
            frame_filename = os.path.join(output_folder, f"frame_{frame_count}.jpg")
            cv2.imwrite(frame_filename, frame)

        frame_count += 1

    cap.release()

if __name__ == "__main__":
    video_path = "path/to/your/video.mp4"
    output_folder = "path/to/your/output_frames"
    uniform_sampling(video_path, output_folder)
