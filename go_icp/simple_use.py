import numpy as np;
from py_goicp import GoICP, POINT3D, ROTNODE, TRANSNODE;
def loadPointCloud(filename):
    pcloud = np.loadtxt(filename, skiprows=1);
    plist = pcloud.tolist();
    p3dlist = [];
    for x,y,z in plist:
        pt = POINT3D(x,y,z);
        p3dlist.append(pt);
    return pcloud.shape[0], p3dlist;

goicp = GoICP();
Nm, a_points = loadPointCloud('/home/satya/Desktop/MS_project/habitat/go-icp_cython/tests/model_bunny.txt');
Nd, b_points = loadPointCloud('/home/satya/Desktop/MS_project/habitat/go-icp_cython/tests/data_bunny.txt');
goicp.loadModelAndData(Nm, a_points, Nd, b_points);
goicp.setDTSizeAndFactor(300, 2.0);
goicp.BuildDT();
goicp.Register();
print(goicp.optimalRotation()); # A python list of 3x3 is returned with the optimal rotation
print(goicp.optimalTranslation());# A python list of 1x3 is returned with the optimal translation