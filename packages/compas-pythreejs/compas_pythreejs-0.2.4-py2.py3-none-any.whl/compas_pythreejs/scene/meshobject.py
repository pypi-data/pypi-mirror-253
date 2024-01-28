import pythreejs as three
from compas.scene import MeshObject
from compas_pythreejs.scene import ThreeSceneObject


class MeshObject(ThreeSceneObject, MeshObject):
    """Scene object for drawing mesh."""

    def draw(self, color=None):
        """Draw the mesh associated with the scene object.

        Parameters
        ----------
        color : rgb1 | rgb255 | :class:`compas.colors.Color`, optional
            The RGB color of the mesh.

        Returns
        -------
        list[three.Mesh, three.LineSegments]
            List of pythreejs objects created.

        """
        color = self.color if color is None else color
        contrastcolor = color.darkened(50) if color.is_light else color.lightened(50)

        geometry = three.PolyhedronGeometry(
            vertices=self.mesh.vertices_attributes("xyz"),
            faces=list(self.mesh.faces()),
        )

        self._guids = self.geometry_to_objects(geometry, color, contrastcolor)
        return self.guids
