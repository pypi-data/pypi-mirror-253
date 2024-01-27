from pythreejs import Scene as _Scene
from pythreejs import PerspectiveCamera as _PerspectiveCamera
from pythreejs import OrbitControls as _OrbitControls
from pythreejs import Renderer as _Renderer

from IPython.display import display as _display

from compas.plugins import plugin
from compas.colors import Color
from compas.scene import Scene


@plugin(
    category="drawing-utils",
    pluggable_name="after_draw",
    requires=["pythreejs"],
)
def display(scene: Scene, camera=None, controls=None, width=400, height=300, background=None):
    """Display a scene in Jupyter Notebook.

    Parameters
    ----------
    scene : :class:`compas.scene.Scene`
        The scene to display.
    camera : :class:`compas.scene.Camera`, optional
        The camera of the scene.
    controls : :class:`compas.scene.Controls`, optional
        The controls of the scene.
    width : int, optional
        The width of the display.
    height : int, optional
        The height of the display.
    background : str, optional
        The background color of the display.

    Examples
    --------
    >>>

    """
    width = width or 400
    height = height or 300
    aspect = width / height

    if not camera:
        camera = _PerspectiveCamera(position=[0, 0, 10], up=[0, 1, 0], aspect=aspect)

    if not controls:
        controls = _OrbitControls(controlling=camera)

    if not background:
        background = Color.white()

    _scene = _Scene()
    for obj in scene.objects:
        for item in obj.guids:
            print(item)
            _scene.add(item)

    camera.lookAt(_scene.position)
    renderer = _Renderer(scene=_scene, camera=camera, controls=[controls], width=width, height=height)

    _display(renderer)
