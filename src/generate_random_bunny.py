import numpy as np
from mayavi import mlab
import matplotlib.pyplot as plt

plyfile = "../data/bunny/reconstruction/bun_zipper.ply"
n_data = 100

vertex = np.zeros([35947, 5], dtype=float)
face = np.zeros([69451, 3], dtype=int)
with open(plyfile, "r") as f:
    while f.readline().strip() != "end_header":
        pass
    # vertex
    for i in range(35947):
        l = list(map(float, f.readline().strip().split()))
        vertex[i] = l
    # vertex
    for i in range(69451):
        l = list(map(int, f.readline().strip().split()))[1:]
        face[i] = l
vx, vy, vz = vertex[:, :3].T

f = mlab.figure(bgcolor=(0, 0, 0), size=(64, 64))
bunny = mlab.triangular_mesh(vz, vx, vy, face, color=(0.7,)*3)
mlab.view(azimuth=0, elevation=90, distance=0.4)

plt.show()

# z = np.random.uniform(-1, 1, size=n_data)
# phi = np.random.uniform(0, 2*np.pi, size=n_data)
# r = np.sqrt(1 - z*z)
# x, y = r*np.cos(phi), r*np.sin(phi)
# azi_deg, elv_deg = np.rad2deg(phi), np.rad2deg(np.arccos(z))

# img_list = np.empty([n_data, 64, 64, 3])

# for i in range(n_data):
#     mlab.view(azimuth=azi_deg[i], elevation=elv_deg[i], distance=0.4)
#     img_list[i] = mlab.screenshot()/255.

# np.savez_compressed("bunny_image", img_list)