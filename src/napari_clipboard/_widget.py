"""
This module is an example of a barebones QWidget plugin for napari

It implements the Widget specification.
see: https://napari.org/stable/plugins/guides.html?#widgets

Replace code below according to your needs.
"""
from magicgui import magic_factory
from qtpy.QtWidgets import QApplication

import numpy as np

import napari

# TODO figure out if the button can be disabled
@magic_factory(layout="horizontal", call_button="New Image from Clipboard")
def image_from_clipboard(viewer: "napari.viewer.Viewer"):

    clipboard = QApplication.instance().clipboard()

    mime_data = clipboard.mimeData()

    if mime_data.hasImage():

        image = mime_data.imageData()
        ptr = image.bits()
        ptr.setsize(image.byteCount())
        arr = np.array(ptr).reshape(image.height(), image.width(), 4)  # 4 for RGBA
        
        viewer.add_image(arr)
    
    else:
        napari.utils.notifications.show_info("Cannot create layer from current clipboard contents.")
