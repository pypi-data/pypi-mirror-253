import pythreejs as three

from compas.scene import GeometryObject
from compas.colors import Color
from compas_pythreejs.conversions import box_to_threejs
from .sceneobject import ThreeSceneObject


class BoxObject(ThreeSceneObject, GeometryObject):
    """Scene object for drawing box shapes."""

    def draw(self, color=None):
        """Draw the box associated with the scene object.

        Parameters
        ----------
        color : rgb1 | rgb255 | :class:`compas.colors.Color`, optional
            The RGB color of the box.

        Returns
        -------
        list[three.Mesh, three.LineSegments]
            List of pythreejs objects created.

        """
        color = Color.coerce(color) or self.color
        contrastcolor: Color = color.darkened(50) if color.is_light else color.lightened(50)

        geometry = box_to_threejs(self.geometry)

        edges = three.EdgesGeometry(geometry)
        mesh = three.Mesh(geometry, three.MeshBasicMaterial(color=color.hex))
        line = three.LineSegments(edges, three.LineBasicMaterial(color=contrastcolor.hex))

        self._guids = [mesh, line]
        return self.guids
