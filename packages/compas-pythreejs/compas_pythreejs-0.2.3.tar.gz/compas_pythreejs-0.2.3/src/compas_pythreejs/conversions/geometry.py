from compas.geometry import Box
from pythreejs import BoxGeometry


def box_to_threejs(box: Box) -> BoxGeometry:
    """Convert a COMPAS box to a PyThreeJS box geometry.

    Parameters
    ----------
    box : :class:`compas.geometry.Box`
        The box to convert.

    Returns
    -------
    :class:`pythreejs.BoxGeometry`
        The PyThreeJS box geometry.

    Examples
    --------
    >>> from compas.geometry import Box
    >>> box = Box.from_width_height_depth(1, 2, 3)
    >>> box_to_threejs(box)
    BoxGeometry(depth=3.0, height=2.0)

    """
    return BoxGeometry(width=box.width, height=box.height, depth=box.depth)
