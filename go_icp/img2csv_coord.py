# # Generating the txt file for image point cloud of size 800x abc


# import cv2
# import numpy as np
# import pandas as pd
# import os
# import msgpack
# import open3d as o3d
# import matplotlib.image as mpimg
# import copy



# def extract_canny_coordinates(canny_image, constant_y=2):
#     coordinates = []
#     rows, cols = canny_image.shape

#     for x in range(cols):
#         for z in range(rows):
#             if canny_image[z, x] > 0:  # Check if pixel intensity is greater than 0 (edge pixel)
#                 coordinates.append([x, constant_y, z])

#     return np.array(coordinates)


# def save_coordinates(coordinates, output_path):
#     # Save the x, y, z coordinates to the specified output path
#     np.savetxt(output_path, coordinates, fmt='%d', delimiter=',', header='', comments='')

# def process_rgb_image(rgb_image_path):
    
#     # Read the RGB image
#     rgb_image = cv2.imread(rgb_image_path, cv2.IMREAD_UNCHANGED)

#     # Check if the image is loaded successfully
#     if rgb_image is None:
#         raise ValueError(f"Error loading image from path: {rgb_image_path}")

#     # Print additional information about the image
#     print(f"Shape of the input image: {rgb_image.shape}")

#     # Visualize the mirrored, blurred, and edge-detected image with a window size of 800xabc
#     canny_image = visualize_image(rgb_image, window_name='Mirrored, Blurred, and Edge Detected Image')

#     # Extract x, y, z coordinates from the Canny edge image
#     coordinates = extract_canny_coordinates(canny_image, constant_y=2)

#     # Save the coordinates to a TXT file
#     file_name = os.path.splitext(os.path.basename(rgb_image_path))
#     txt_file_path = (f"{os.path.dirname(rgb_image_path)}/{file_name[0]}_image.txt")
#     np.savetxt(txt_file_path, coordinates, fmt='%e', delimiter=' ')
#     print(f"Converted TXT data saved as {txt_file_path}")




# if __name__ == "__main__":


#     rgb_image_path = "/mnt/data/sam/Mowito/test_images/template_mask.jpg"

#     # Process RGB image
#     process_rgb_image(rgb_image_path)



# Generating the txt file for image point cloud of size 800x abc


import cv2
import numpy as np
import pandas as pd
import os
import msgpack
import open3d as o3d
import matplotlib.image as mpimg
import copy



def extract_canny_coordinates(canny_image, constant_y=2):
    coordinates = []
    rows, cols = canny_image.shape

    for x in range(cols):
        for z in range(rows):
            if canny_image[z, x] > 0:  # Check if pixel intensity is greater than 0 (edge pixel)
                coordinates.append([x, constant_y, z])

    return np.array(coordinates)

def visualize_image(image, window_name='Image'):
    
    print("image_shape:", image.shape)

    _ = 800/image.shape[1]

    window_size = int(image.shape[1]*_), int(image.shape[0]*_)
    print("window_size:", window_size)

    # Resize the image to the specified window size
    resized_image = cv2.resize(image, window_size)

   
    # No Mirror the image horizontally
    mirrored_image = resized_image

    # Apply Gaussian blur
    blur = cv2.GaussianBlur(mirrored_image, (5,5), cv2.BORDER_DEFAULT)

    # Perform Canny edge detection
    canny = cv2.Canny(blur, 10, 300)

    # Display the resized image
    cv2.imshow(window_name, canny)
    cv2.waitKey(7000)
    cv2.destroyAllWindows()

    return canny

def save_coordinates(coordinates, output_path):
    # Save the x, y, z coordinates to the specified output path
    np.savetxt(output_path, coordinates, fmt='%d', delimiter=',', header='', comments='')

def process_rgb_image(rgb_image_path):
    
    # Read the RGB image
    rgb_image = cv2.imread(rgb_image_path, cv2.IMREAD_UNCHANGED)

    # Check if the image is loaded successfully
    if rgb_image is None:
        raise ValueError(f"Error loading image from path: {rgb_image_path}")

    # Print additional information about the image
    print(f"Shape of the input image: {rgb_image.shape}")

    # Visualize the mirrored, blurred, and edge-detected image with a window size of 800xabc
    canny_image = visualize_image(rgb_image, window_name='Mirrored, Blurred, and Edge Detected Image')

    # Extract x, y, z coordinates from the Canny edge image
    coordinates = extract_canny_coordinates(canny_image, constant_y=2)

    # Save the coordinates to a TXT file
    file_name = os.path.splitext(os.path.basename(rgb_image_path))
    txt_file_path = (f"{os.path.dirname(rgb_image_path)}/{file_name[0]}_image.txt")
    np.savetxt(txt_file_path, coordinates, fmt='%e', delimiter=' ')
    print(f"Converted TXT data saved as {txt_file_path}")




if __name__ == "__main__":


    rgb_image_path = "/mnt/data/sam/Mowito/template_images/template.jpg"  # image path


    # Process RGB image
    process_rgb_image(rgb_image_path)

