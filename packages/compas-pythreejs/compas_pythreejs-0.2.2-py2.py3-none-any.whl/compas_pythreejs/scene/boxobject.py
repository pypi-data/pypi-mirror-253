from pythreejs import Mesh
from pythreejs import EdgesGeometry
from pythreejs import LineSegments
from pythreejs import MeshBasicMaterial
from pythreejs import LineBasicMaterial

from compas.scene import GeometryObject
from compas.colors import Color
from compas_pythreejs.conversions import box_to_threejs
from .sceneobject import PyThreeJSSceneObject


class BoxObject(PyThreeJSSceneObject, GeometryObject):
    """Scene object for drawing box shapes.

    Parameters
    ----------
    box : :class:`compas.geometry.Box`
        A COMPAS box.
    **kwargs : dict, optional
        Additional keyword arguments.

    """

    def __init__(self, box, **kwargs):
        super(BoxObject, self).__init__(geometry=box, **kwargs)
        self.box = box

    def draw(self, color=None):
        """Draw the box associated with the scene object.

        Parameters
        ----------
        color : rgb1 | rgb255 | :class:`compas.colors.Color`, optional
            The RGB color of the box.

        Returns
        -------
        list[System.Guid]
            List of GUIDs of the objects created in Rhino.

        """
        color = Color.coerce(color) or self.color
        geometry = box_to_threejs(self.geometry)
        edges = EdgesGeometry(geometry)

        mesh = Mesh(geometry, MeshBasicMaterial(color=color.hex))
        line = LineSegments(edges, LineBasicMaterial(color=color.darkened(50).hex))

        self._guids = [mesh, line]
        return self.guids
