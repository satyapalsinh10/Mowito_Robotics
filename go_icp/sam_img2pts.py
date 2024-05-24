import os
import numpy as np
import torch
import cv2
import supervision as sv
from segment_anything import sam_model_registry, SamAutomaticMaskGenerator, SamPredictor
from PIL import Image
from scipy.stats import zscore
import open3d as o3d


# Define paths

CHECKPOINT_PATH = "/mnt/data/sam/Mowito/go_icp/sam_weights/sam_vit_h_4b8939.pth"
HOME = "/mnt/data/sam/Mowito/test_images"
IMAGE_NAME = "template.jpg"
IMAGE_PATH = os.path.join(HOME, IMAGE_NAME)
print(IMAGE_PATH)

# Check device
DEVICE = torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')
MODEL_TYPE = "vit_h"

# Load model
sam = sam_model_registry[MODEL_TYPE](checkpoint=CHECKPOINT_PATH).to(device=DEVICE)
mask_predictor = SamPredictor(sam)

# Default box
default_box = {'x': 1, 'y': 1, 'width': 1920, 'height': 1080, 'label': ''}
box = default_box
box = np.array([box['x'], box['y'], box['x'] + box['width'], box['y'] + box['height']])

# Read and preprocess image
image_bgr = cv2.imread(IMAGE_PATH)
image_rgb = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2RGB)

mask_predictor.set_image(image_rgb)

masks, scores, logits = mask_predictor.predict(
    box=box,
    multimask_output=True
)

# Annotate images
box_annotator = sv.BoxAnnotator(color=sv.Color.RED)
mask_annotator = sv.MaskAnnotator(color=sv.Color.RED, color_lookup=sv.ColorLookup.INDEX)
detections = sv.Detections(
    xyxy=sv.mask_to_xyxy(masks=masks),
    mask=masks
)
detections = detections[detections.area == np.max(detections.area)]

# Generate annotated images
source_image = box_annotator.annotate(scene=image_bgr.copy(), detections=detections, skip_label=True)
segmented_image = mask_annotator.annotate(scene=image_bgr.copy(), detections=detections)

# Assuming 'masks' is your list of masks
last_mask = masks[-1]  # Select the last mask and put it in a list

final_mask = np.logical_not(last_mask)

# Convert the boolean array to an 8-bit integer array
binary_image_array = (final_mask * 255).astype(np.uint8)

crop_pixels = 5
final_array = binary_image_array[crop_pixels:-crop_pixels, crop_pixels:-crop_pixels]


# print(binary_image.dtype)

print(final_array.shape)
print(final_array[220:225,220:225])

# Create an image from the array
final_image = Image.fromarray(final_array)

# Save the cropped image
final_image.save(f'{HOME}/mask_{IMAGE_NAME}')


# Convert the image to points .txt
constant_y = 2
coordinates = []

rows, cols = final_array.shape

# Iterate through each pixel in the image
for x in range(cols):
    for z in range(rows):
        # Check if the pixel value exceeds a threshold (125 in this case)
        if final_array[z, x] > 125:
            # Append the coordinates to the list
            coordinates.append([x, z, constant_y])

# Convert the list of coordinates to a NumPy array
coordinates_array = np.array(coordinates)

# Create a point cloud from the data
pcd = o3d.geometry.PointCloud()
pcd.points = o3d.utility.Vector3dVector(coordinates_array)

# Outlier removal using statistical method
cl, ind = pcd.remove_statistical_outlier(nb_neighbors=1000, std_ratio=0.1)

# Select inliers
inliers = pcd.select_by_index(ind)

# Convert inliers to NumPy array
filtered_coordinates_array = np.asarray(inliers.points)

# Save the filtered coordinates to a text file
output_path = f'/mnt/data/sam/Mowito/test_images/{os.path.splitext(IMAGE_NAME)[0]}_coordinates.txt'
np.savetxt(output_path, filtered_coordinates_array, fmt='%.2f', delimiter=' ', header='', comments='')

print(f"Filtered coordinates TXT data saved as {output_path}")






