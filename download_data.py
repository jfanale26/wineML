import kagglehub
import os
import shutil

# Get current project directory
project_dir = os.getcwd()
dataset_dir = os.path.join(project_dir, "wine_dataset")

# Download latest version to default location first
print("Downloading dataset...")
path = kagglehub.dataset_download("zynicide/wine-reviews")

print("Original download path:", path)

# Create the target directory if it doesn't exist
if not os.path.exists(dataset_dir):
    os.makedirs(dataset_dir)

# Copy all files from the downloaded location to our project directory
print(f"Copying files to {dataset_dir}...")
for item in os.listdir(path):
    source = os.path.join(path, item)
    destination = os.path.join(dataset_dir, item)
    
    if os.path.isfile(source):
        shutil.copy2(source, destination)
    elif os.path.isdir(source):
        shutil.copytree(source, destination, dirs_exist_ok=True)

print("Dataset successfully copied to:", dataset_dir)
print("Files in project directory:")
for item in os.listdir(dataset_dir):
    print(f"  - {item}")