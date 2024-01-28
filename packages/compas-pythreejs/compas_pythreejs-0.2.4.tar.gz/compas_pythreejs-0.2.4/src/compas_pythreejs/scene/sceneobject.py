import pythreejs as three
from compas.scene import SceneObject


class ThreeSceneObject(SceneObject):
    """Base class for all PyThreeJS scene objects."""

    def geometry_to_objects(self, geometry, color, contrastcolor):
        """Convert a PyThreeJS geometry to a list of PyThreeJS objects.

        Parameters
        ----------
        geometry : :class:`three.Geometry`
            The PyThreeJS geometry to convert.
        color : rgb1 | rgb255 | :class:`compas.colors.Color`
            The RGB color of the geometry.
        contrastcolor : rgb1 | rgb255 | :class:`compas.colors.Color`
            The RGB color of the edges.

        Returns
        -------
        list[three.Mesh, three.LineSegments]
            List of PyThreeJS objects created.

        """
        edges = three.EdgesGeometry(geometry)
        mesh = three.Mesh(geometry, three.MeshBasicMaterial(color=color.hex))
        line = three.LineSegments(edges, three.LineBasicMaterial(color=contrastcolor.hex))
        return [mesh, line]
