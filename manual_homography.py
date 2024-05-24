import cv2
import numpy as np

# Global variables to store selected points and current image being selected
template_points = []
test_points = []
selecting_template = True  # Start by selecting points on the template image

# Mouse callback function
def select_points(event, x, y, flags, param):
    global template_points, test_points, selecting_template
    if event == cv2.EVENT_LBUTTONDOWN:
        if selecting_template:
            template_points.append((x, y))
            cv2.circle(template_disp, (x, y), 5, (0, 255, 0), -1)
            cv2.imshow("Template Image", template_disp)
        else:
            test_points.append((x, y))
            cv2.circle(test_disp, (x, y), 5, (0, 255, 0), -1)
            cv2.imshow("Test Image", test_disp)

# Read the template and test images
template = cv2.imread("/mnt/data/sam/Mowito/test_images/template.jpg")
test_img = cv2.imread("/mnt/data/sam/Mowito/test_images/test_1.jpg")


template = cv2.resize(template, (0, 0), fx=1/2, fy=1/2)
test_img = cv2.resize(test_img, (0, 0), fx=1/2, fy=1/2)
template_disp = template.copy()
test_disp = test_img.copy()
cv2.imshow("Template Image", template_disp)
cv2.setMouseCallback("Template Image", select_points)

# Wait for the user to select points and switch between images
while True:
    key = cv2.waitKey(1) & 0xFF
    if key == ord('n'):  # Press 'n' to switch to the test image
        selecting_template = False
        cv2.imshow("Test Image", test_disp)
        cv2.setMouseCallback("Test Image", select_points)
    elif key == ord('q'):  # Press 'q' to finish selection
        break

cv2.destroyAllWindows()

# Convert selected points to numpy arrays
template_pts = np.float32(template_points).reshape(-1, 1, 2)
test_pts = np.float32(test_points).reshape(-1, 1, 2)
M, _ = cv2.findHomography(template_pts, test_pts, cv2.RANSAC)
angle = np.arctan2(M[0, 1], M[0, 0]) * 180 / np.pi


print("Rotation Angle:", angle)