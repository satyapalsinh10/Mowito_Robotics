# Mowito_Robotics

## Methond_1 : `Manual_Homography`

### Prerequisites
 - Python 3.x
 - OpenCV
 - NumPy

### Installation steps

- **Clone the repository:**

`git clone https://github.com/satyapalsinh10/Mowito_Robotics.git`

`cd /Mowito_Robotics`


- **Install the required packages:**

`pip install numpy`

`pip install opencv-python`


### Usage

- **Run the script:**

`python manual_homography.py`

1. A window displaying the template image will appear. Click on corresponding points on the template image. Each click will mark a point with a green circle.

2. Press the 'n' key to switch to the test image. Select the corresponding points on the test image.

3. Press the 'q' key when you are done selecting points.

4. The script will compute the homography matrix and print the rotation angle between the template and test images.


---

---


## Methond_2 : `Auto_Homography`

### Prerequisites
 - Python 3.x
 - OpenCV
 - NumPy

### Usage

- **Run the script:**

`python auto_homography.py`


### Theory

- **Read Images:** Read grayscale template and test images.
- **Detect Keypoints:** Use ORB detector to find keypoints and descriptors.
- **Match Keypoints:** Match keypoints between template and test images using Brute-Force Matcher.
- **Draw Matches:** Draw top matching keypoints on a new image.
- **Estimate Homography:** Compute homography matrix using RANSAC algorithm.
- **Transform Corners:** Apply perspective transformation to template corners to find corresponding corners in the test image.
- **Calculate Rotation Angle:** Determine rotation angle by finding the angle of the minimum area rectangle enclosing transformed corners.
- **Display Result:** Display the matched image with keypoints and matches drawn on it.

---

---



## Methond_3 : `Point_CLoud_Registration Using GO-ICP`

You can find more about Go-ICP Cython implementation [here](https://github.com/aalavandhaann/go-icp_cython).

### Installation Instructions

`cd go-icp_cython`

`pip install opencv-python`

`pip install pandas`

`pip install open3d`

`pip install matplotlib`

`pip install cython`

`python setup.py build_ext --inplace`

`python setup.py install`

`pip install py-goicp`


### Usage

- **Run the script:**

1. `python img2csv_coord.py` - **Run this step for both the `template.jpg` and `test.jpg` to generate independent .txt files consisting all the points which will be used in the following steps.**

2. `python test.py` - **Implement the template.txt and test.txt path in the file and run the file to generate the final rotation using ICP**

3. `python visualizer_transf.py`  - **Implement the template.txt path and a data_transformed.ply file path and run this file to visualize the final ICP registered**











