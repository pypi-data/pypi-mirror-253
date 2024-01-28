import pythreejs as three

from IPython.display import display as ipydisplay

from compas.plugins import plugin
from compas.colors import Color


@plugin(
    category="drawing-utils",
    pluggable_name="after_draw",
    requires=["pythreejs"],
)
def display(objects, camera3=None, controls3=None, width=400, height=300, background=None):
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

    if not camera3:
        camera3 = three.PerspectiveCamera(position=[0, 0, 10], up=[0, 1, 0], aspect=aspect)

    if not controls3:
        controls3 = three.OrbitControls(controlling=camera3)

    if not background:
        background = Color.white()

    scene3 = three.Scene()
    for obj in objects:
        scene3.add(obj)

    camera3.lookAt(scene3.position)
    renderer3 = three.Renderer(scene=scene3, camera=camera3, controls=[controls3], width=width, height=height)

    # print(renderer3)
    ipydisplay(renderer3)
