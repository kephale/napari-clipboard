import numpy as np

from napari_clipboard import image_from_clipboard

def test_image_from_clipboard(make_napari_viewer, capsys):
    viewer = make_napari_viewer()

    # this time, our widget will be a MagicFactory or FunctionGui instance
    my_widget = image_from_clipboard()    

    # if we "call" this object, it'll execute our function
    my_widget(viewer)

