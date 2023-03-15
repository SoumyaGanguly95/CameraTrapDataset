import os
import random
import shutil

# Define paths for source images and labels, and target train/validation/test folders
image_dir = 'D:/MyWorkspace/CameraTrapChallenge/object_detection_with_custom_yoloV7/data_prep/data'
label_dir = 'D:/MyWorkspace/CameraTrapChallenge/object_detection_with_custom_yoloV7/data_prep/labels'
train_dir = 'D:/MyWorkspace/CameraTrapChallenge/object_detection_with_custom_yoloV7/data_prep/output/train'
val_dir = 'D:/MyWorkspace/CameraTrapChallenge/object_detection_with_custom_yoloV7/data_prep/output/val'
test_dir = 'D:/MyWorkspace/CameraTrapChallenge/object_detection_with_custom_yoloV7/data_prep/output/test'

# Define split ratios (70% train, 15% validation, 15% test)
train_ratio = 0.7
val_ratio = 0.15
test_ratio = 0.15

# Get list of image and label files
image_files = os.listdir(image_dir)
label_files = os.listdir(label_dir)

# Zip the image and label files together for shuffling
file_pairs = list(zip(image_files, label_files))
random.shuffle(file_pairs)

# Calculate split indices
num_files = len(file_pairs)
train_index = int(num_files * train_ratio)
val_index = train_index + int(num_files * val_ratio)

# Create target directories if they don't already exist
os.makedirs(train_dir, exist_ok=True)
os.makedirs(val_dir, exist_ok=True)
os.makedirs(test_dir, exist_ok=True)

# Move files to train, validation, and test directories
for i, (image_file, label_file) in enumerate(file_pairs):
    if i < train_index:
        shutil.copy(os.path.join(image_dir, image_file),
                    os.path.join(train_dir, image_file))
        shutil.copy(os.path.join(label_dir, label_file),
                    os.path.join(train_dir, label_file))
    elif i < val_index:
        shutil.copy(os.path.join(image_dir, image_file),
                    os.path.join(val_dir, image_file))
        shutil.copy(os.path.join(label_dir, label_file),
                    os.path.join(val_dir, label_file))
    else:
        shutil.copy(os.path.join(image_dir, image_file),
                    os.path.join(test_dir, image_file))
        shutil.copy(os.path.join(label_dir, label_file),
                    os.path.join(test_dir, label_file))
