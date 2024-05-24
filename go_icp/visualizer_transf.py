import open3d as o3d
import numpy as np
import os


def load_point_cloud(filename, color):
    points = np.loadtxt(filename, skiprows=1)
    pc = o3d.geometry.PointCloud(o3d.utility.Vector3dVector(points))
    pc.paint_uniform_color(color)
    return pc

def load_point_cloud_ply(filename, color):
    ply_data = o3d.io.read_point_cloud(filename)
    ply_data.paint_uniform_color(color)
    return ply_data

def visualize_point_clouds(point_clouds):
    o3d.visualization.draw_geometries(point_clouds)

if __name__ == "__main__":
    
    model_file_path = "/mnt/data/sam/Mowito/test_images/template_coordinates.txt"  # image.txt  
    transformed_file_path = f"{os.path.dirname(model_file_path)}/data_transformed.ply" # transformed.ply

    # Load and color the point clouds
    model_point_cloud = load_point_cloud(model_file_path, [0, 0, 1])  # Blue color for model_point_cloud
    transformed_point_cloud = load_point_cloud_ply(transformed_file_path, [0, 1, 0])  # Green color for transformed_point_cloud

    # Visualize all point clouds in the same window
    # visualize_point_clouds([model_point_cloud])
    visualize_point_clouds([model_point_cloud, transformed_point_cloud])
