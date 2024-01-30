def cut_pcd(points, pcd_range):
    x_range = [pcd_range[0], pcd_range[3]]
    y_range = [pcd_range[1], pcd_range[4]]
    z_range = [pcd_range[2], pcd_range[5]]
    mask = (x_range[0] <= points[:, 0]) & (points[:, 0] <= x_range[1]) & (y_range[0] < points[:, 1]) & (
            points[:, 1] <= y_range[1]) & (z_range[0] < points[:, 2]) & (points[:, 2] <= z_range[1])
    points = points[mask]
    return points