import kagglehub

# Download latest version
path = kagglehub.dataset_download("zynicide/wine-reviews")

print("Path to dataset files:", path)