from compas.scene import SceneObject


class PyThreeJSSceneObject(SceneObject):
    """Base class for all PyThreeJS scene objects.

    Parameters
    ----------
    **kwargs : dict, optional
        Additional keyword arguments.

    """

    def __init__(self, **kwargs):
        super(PyThreeJSSceneObject, self).__init__(**kwargs)
