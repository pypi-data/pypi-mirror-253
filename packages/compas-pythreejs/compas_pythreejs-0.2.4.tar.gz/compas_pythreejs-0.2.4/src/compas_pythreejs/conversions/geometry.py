import pythreejs as three
from compas.geometry import Box
from compas.geometry import Cone
from compas.geometry import Cylinder
from compas.geometry import Sphere
from compas.geometry import Torus


def box_to_threejs(box: Box) -> three.BoxGeometry:
    """Convert a COMPAS box to a PyThreeJS box geometry.

    Parameters
    ----------
    box : :class:`compas.geometry.Box`
        The box to convert.

    Returns
    -------
    :class:`three.BoxGeometry`
        The PyThreeJS box geometry.

    Examples
    --------
    >>> from compas.geometry import Box
    >>> box = Box.from_width_height_depth(1, 2, 3)
    >>> box_to_threejs(box)
    BoxGeometry(depth=3.0, height=2.0)

    """
    return three.BoxGeometry(width=box.width, height=box.height, depth=box.depth)


def cone_to_threejs(cone: Cone) -> three.CylinderGeometry:
    """Convert a COMPAS cone to a PyThreeJS cone geometry.

    Parameters
    ----------
    cone : :class:`compas.geometry.Cone`
        The cone to convert.

    Returns
    -------
    :class:`three.CylinderGeometry`
        The PyThreeJS cone geometry.

    Examples
    --------
    >>> from compas.geometry import Cone
    >>> cone = Cone(radius=1, height=2)
    >>> cone_to_threejs(cone)
    CylinderGeometry(height=2.0, radiusTop=0.0)

    """
    return three.CylinderGeometry(radiusTop=0, radiusBottom=cone.radius, height=cone.height)


def cylinder_to_threejs(cylinder: Cylinder) -> three.CylinderGeometry:
    """Convert a COMPAS cylinder to a PyThreeJS cylinder geometry.

    Parameters
    ----------
    cylinder : :class:`compas.geometry.Cylinder`
        The cylinder to convert.

    Returns
    -------
    :class:`three.CylinderGeometry`
        The PyThreeJS cylinder geometry.

    Examples
    --------
    >>> from compas.geometry import Cylinder
    >>> cylinder = Cylinder(radius=1, height=2)
    >>> cylinder_to_threejs(cylinder)
    CylinderGeometry(height=2.0)

    """
    return three.CylinderGeometry(radiusTop=cylinder.radius, radiusBottom=cylinder.radius, height=cylinder.height)


def sphere_to_threejs(sphere: Sphere) -> three.SphereGeometry:
    """Convert a COMPAS sphere to a PyThreeJS sphere geometry.

    Parameters
    ----------
    sphere : :class:`compas.geometry.Sphere`
        The sphere to convert.

    Returns
    -------
    :class:`three.SphereGeometry`
        The PyThreeJS sphere geometry.

    Examples
    --------
    >>> from compas.geometry import Sphere
    >>> sphere = Sphere(radius=1)
    >>> sphere_to_threejs(sphere)
    SphereGeometry()

    """
    return three.SphereGeometry(radius=sphere.radius)


def torus_to_threejs(torus: Torus) -> three.TorusGeometry:
    """Convert a COMPAS torus to a PyThreeJS torus geometry.

    Parameters
    ----------
    torus : :class:`compas.geometry.Torus`
        The torus to convert.

    Returns
    -------
    :class:`three.TorusGeometry`
        The PyThreeJS torus geometry.

    Examples
    --------
    >>> from compas.geometry import Torus
    >>> torus = Torus(radius_axis=1, radius_pipe=0.2)
    >>> torus_to_threejs(torus)
    TorusGeometry(tube=0.2)

    """
    return three.TorusGeometry(radius=torus.radius_axis, tube=torus.radius_pipe)
