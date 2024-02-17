import shutil
import numpy as np
import cv2
import os
from keras.applications import VGG16 
from keras.models import Model
import config


def ensure_directory_exists(data):
    if not os.path.exists(data):
        os.makedirs(data)

def video_to_frames(video):
    path = os.path.join(config.test_path, 'temporary_images')
    if os.path.exists(path):
        shutil.rmtree(path)
    ensure_directory_exists(path)
    video_path = os.path.join(config.test_path, 'video', video)
    count = 0
    image_list = []

    # Path to video file
    cap = cv2.VideoCapture(video_path)
    while cap.isOpened():
        ret, frame = cap.read()
        if ret is False:
            break
        cv2.imwrite(os.path.join(config.test_path, 'temporary_images', 'frame%d.jpg' % count), frame)
        image_list.append(os.path.join(config.test_path, 'temporary_images', 'frame%d.jpg' % count))
        count += 1

    cap.release()
    cv2.destroyAllWindows()
    return image_list

def extract_features(video, model):
    video_id = video.split(".")[0]
    print(video_id)
    print(f'Processing video {video}')

    # Ensure consistent order of frames
    image_list = sorted(video_to_frames(video))

    samples = np.round(np.linspace(0, len(image_list) - 1, 80))
    image_list = [image_list[int(sample)] for sample in samples]
    images = np.zeros((len(image_list), 224, 224, 3))
    
    for i in range(len(image_list)):
        img = load_image(image_list[i])
        images[i] = img
    
    images = np.array(images)
    fc_feats = model.predict(images, batch_size=128)
    img_feats = np.array(fc_feats)
    
    # cleanup
    shutil.rmtree(os.path.join(config.test_path, 'temporary_images'))
    return img_feats

def load_image(path):
    img = cv2.imread(path)
    img = cv2.resize(img, (224, 224))
    return img

def model_cnn_load():
    model = VGG16(weights="imagenet", include_top=True, input_shape=(224, 224, 3))
    out = model.layers[-2].output
    model_final = Model(inputs=model.input, outputs=out)
    return model_final

def extract_feats_pretrained_cnn():
    model = model_cnn_load()
    print('Model loaded')

    ensure_directory_exists(os.path.join(config.test_path, 'feat')) 

    # Ensure consistent order of videos
    video_list = sorted(os.listdir(os.path.join(config.test_path, 'video')))
    
    for video in video_list:
        outfile = os.path.join(config.test_path, 'feat', video + '.npy')
        img_feats = extract_features(video, model)
        np.save(outfile, img_feats)

if __name__ == "__main__":
    extract_feats_pretrained_cnn()