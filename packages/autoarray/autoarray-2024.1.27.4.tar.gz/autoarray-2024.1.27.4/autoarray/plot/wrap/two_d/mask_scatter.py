from autoarray.plot.wrap.two_d.grid_scatter import GridScatter


class MaskScatter(GridScatter):
    """
    Plots a mask over an image, using the `Mask2d` object's (y,x) `edge_sub_1` property.

    See `wrap.base.Scatter` for a description of how matplotlib is wrapped to make this plot.
    """
