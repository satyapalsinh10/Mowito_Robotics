import cv2
import numpy as np


# Read the template and test images
template = cv2.imread("/mnt/data/sam/Mowito/template_images/template.jpg", cv2.IMREAD_GRAYSCALE)
test_img = cv2.imread("/mnt/data/sam/Mowito/test_images/test_2.jpg", cv2.IMREAD_GRAYSCALE)

# Initialize ORB detector
orb = cv2.ORB_create()

# Detect keypoints and descriptors for the template and test images
template_kp, template_des = orb.detectAndCompute(template, None)
test_kp, test_des = orb.detectAndCompute(test_img, None)

# Create a Brute-Force Matcher
bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

# Match keypoints between the template and test images
matches = bf.match(template_des, test_des)
matches = sorted(matches, key=lambda x: x.distance)

# Draw matches
matched_img = cv2.drawMatches(template, template_kp, test_img, test_kp, matches[:20], None, flags=cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)

# Extract matched keypoints' coordinates
template_pts = np.float32([template_kp[m.queryIdx].pt for m in matches]).reshape(-1, 1, 2)
test_pts = np.float32([test_kp[m.trainIdx].pt for m in matches]).reshape(-1, 1, 2)

# Find homography between the template and test keypoints
M, _ = cv2.findHomography(template_pts, test_pts, cv2.RANSAC)

# Apply perspective transformation to the corners of the template image
corners = np.float32([[0, 0], [0, template.shape[0]], [template.shape[1], template.shape[0]], [template.shape[1], 0]]).reshape(-1, 1, 2)
transformed_corners = cv2.perspectiveTransform(corners, M)

# Calculate the angle of rotation
rect = cv2.minAreaRect(transformed_corners)
print(rect)
angle = rect[2]

# Print the rotation angle
print("Rotation Angle:", angle)

# Resize the matched image
scaled_matched_img = cv2.resize(matched_img, (0, 0), fx=0.3, fy=0.3)  # Adjust the scaling factor as needed


# Display the output
cv2.imshow("matched images",scaled_matched_img)
cv2.waitKey(0)
cv2.destroyAllWindows()



