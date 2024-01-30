# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class DashPaperdragon(Component):
    """A DashPaperdragon component.


Keyword arguments:

- id (string; optional):
    The ID used to identify this component in Dash callbacks.

- curMousePosition (dict; optional):
    Current Mouse Position in Image Coordinates.

- curShapeObject (dict; optional):
    curShapeObject is the current shape object that was most recently
    moused over.

- shapeList (dict; optional):
    shapeList is a list of shapes to be drawn on the image.

- tileSourceProps (list; optional):
    FOR DEV: Array of properties to set for each tile Source.

- tileSources (string | list; optional):
    the tile source for openseadragon.

- viewPortBounds (dict; optional):
    viewportBounds of the current OSD Viewer.

- viewerHeight (number; optional)

- viewerWidth (number; optional):
    Dash-assigned callback that should be called to report property
    changes to Dash, to make them available for callbacks.

- zoomLevel (number; optional):
    zoomLevel of the current OSD Viewer."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'dash_paperdragon'
    _type = 'DashPaperdragon'
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, shapeList=Component.UNDEFINED, tileSources=Component.UNDEFINED, tileSourceProps=Component.UNDEFINED, zoomLevel=Component.UNDEFINED, curMousePosition=Component.UNDEFINED, viewPortBounds=Component.UNDEFINED, curShapeObject=Component.UNDEFINED, viewerWidth=Component.UNDEFINED, viewerHeight=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'curMousePosition', 'curShapeObject', 'shapeList', 'tileSourceProps', 'tileSources', 'viewPortBounds', 'viewerHeight', 'viewerWidth', 'zoomLevel']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'curMousePosition', 'curShapeObject', 'shapeList', 'tileSourceProps', 'tileSources', 'viewPortBounds', 'viewerHeight', 'viewerWidth', 'zoomLevel']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(DashPaperdragon, self).__init__(**args)
