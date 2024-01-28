import pythreejs as three
from compas.scene import GeometryObject
from compas.colors import Color
from .sceneobject import ThreeSceneObject


class PolyhedronObject(ThreeSceneObject, GeometryObject):
    """Scene object for drawing polyhedron."""

    def draw(self, color: Color = None):
        """Draw the polyhedron associated with the scene object.

        Parameters
        ----------
        color : rgb1 | rgb255 | :class:`compas.colors.Color`, optional
            The RGB color of the polyhedron.

        Returns
        -------
        list[three.Mesh, three.LineSegments]
            List of pythreejs objects created.

        """
        color: Color = Color.coerce(color) or self.color
        contrastcolor: Color = color.darkened(50) if color.is_light else color.lightened(50)

        polyhedron = three.PolyhedronGeometry(
            vertices=self.geometry.vertices,
            faces=self.geometry.faces,
        )

        self._guids = self.geometry_to_objects(polyhedron, color, contrastcolor)
        return self.guids
