import open3d as o3d
import numpy as np

def load_point_cloud(filename, color):
    points = np.loadtxt(filename, skiprows=1)
    pc = o3d.geometry.PointCloud(o3d.utility.Vector3dVector(points))
    pc.paint_uniform_color(color)
    return pc

def visualize_point_clouds(point_clouds):
    o3d.visualization.draw_geometries(point_clouds)

if __name__ == "__main__":
    # Paths to the data_bunny.txt and model_bunny.txt files
    data_file_path = "/home/satya/Desktop/MS_project/habitat/go-icp_cython/tests/data_bunny.txt"
    model_file_path = "/home/satya/Desktop/MS_project/habitat/go-icp_cython/tests/model_bunny.txt"

    # Load and color the point clouds
    data_point_cloud = load_point_cloud(data_file_path, [1, 0, 0])  # Red color for data_point_cloud
    model_point_cloud = load_point_cloud(model_file_path, [0, 0, 1])  # Blue color for model_point_cloud

    # Visualize both point clouds in the same window
    visualize_point_clouds([data_point_cloud, model_point_cloud])
