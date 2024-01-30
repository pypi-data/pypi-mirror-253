import open3d as o3d
import numpy as np
from pathlib import Path
try:
    from utils.load_pcd import get_points_from_pcd_file
    from utils.o3d_visualize_utils import open3d_draw_scenes, create_mesh_plane, show_pcd_from_points_by_open3d
    from utils.qtopengl_visualize_utils import show_pcd_from_points_by_qtopengl
    from utils import utils
except:
    from .utils.load_pcd import get_points_from_pcd_file
    from .utils.o3d_visualize_utils import open3d_draw_scenes, create_mesh_plane
    from .utils import utils
    from .utils.qtopengl_visualize_utils import show_pcd_from_points_by_qtopengl


class PointCloudProcess:

    @staticmethod
    def cut_pcd(points, pcd_range):
        return utils.cut_pcd(points, pcd_range)

    @staticmethod
    def show_pcd(path, point_size=1, background_color=[0, 0, 0], pcd_range=None, type='open3d'):
        points = PointCloudProcess.get_points(path)[:, 0:3]
        if pcd_range:
            points = utils.cut_pcd(points, pcd_range)
        PointCloudProcess.show_pcd_from_points(points=points, point_size=point_size, background_color=background_color, type=type)

    
    @staticmethod
    def show_pcd_from_points(points, point_size=1, background_color=[0, 0, 0], type='open3d'):
        if type == 'open3d':
            show_pcd_from_points_by_open3d(points=points, point_size=point_size, background_color=background_color)
        elif type == 'qtopengl':
            show_pcd_from_points_by_qtopengl(points=points, point_size=point_size, background_color=background_color)
        elif type == 'mayavi':
            pass
        elif type == 'vispy':
            pass

    @staticmethod
    def get_points(path, num_features=3):
        pcd_ext = Path(path).suffix
        if pcd_ext == '.bin':
            points = np.fromfile(path, dtype=np.float32).reshape(-1, 4)
        elif pcd_ext == ".npy":
            points = np.load(path)
        elif pcd_ext == ".pcd":
            points = get_points_from_pcd_file(path, num_features=num_features)
        else:
            raise NameError("Unable to handle {} formatted files".format(pcd_ext))
        return points[:, 0:num_features]

    @staticmethod
    def add_boxes(points, gt_boxes=None, ref_boxes=None, ref_labels=None, ref_scores=None, point_colors=None,
                  draw_origin=True, type='open3d'):
        if type == 'open3d':
            open3d_draw_scenes(
                points=points,
                gt_boxes=gt_boxes,
                ref_boxes=ref_boxes,
                ref_labels=ref_labels,
                ref_scores=ref_scores,
                point_colors=point_colors,
                draw_origin=draw_origin
            )
        elif type == 'qtopengl':
            pass
        elif type == 'mayavi':
            pass
        elif type == 'vispy':
            pass

if __name__ == '__main__':
    PointCloudProcess.show_pcd(path='data\example\example.pcd',type='qtopengl')
    
