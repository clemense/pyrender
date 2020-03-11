import numpy as np
import trimesh

from pyrender import Viewer, Mesh, PerspectiveCamera, Scene


if __name__ == "__main__":
    bottle_trimesh = trimesh.load('/home/USERNAME/data/ycb/models/021_bleach_cleanser_TMP/textured.obj')
    bottle_mesh = Mesh.from_trimesh(bottle_trimesh)

    cam = PerspectiveCamera(yfov=(np.pi / 3.0))
    cam_pose = np.array([
        [0.0,  -np.sqrt(2)/2, np.sqrt(2)/2, 0.5],
        [1.0, 0.0,           0.0,           0.0],
        [0.0,  np.sqrt(2)/2,  np.sqrt(2)/2, 0.4],
        [0.0,  0.0,           0.0,          1.0]
    ])

    scene = Scene()

    bottle_node = scene.add(bottle_mesh, pose=np.eye(4))

    v = Viewer(scene, shadows=False)

