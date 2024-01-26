# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class DashSign(Component):
    """A DashSign component.
DashSign is a canvas for capturing
hand written signatures

Keyword arguments:

- id (string; optional):
    The ID used to identify this component in Dash callbacks.

- backgroundColor (string; default 'gainsboro'):
    The background color of the signature canvas.

- data (string; optional):
    Base 64 data string for the resulting image.

- n_submit (number; default 0):
    The number of times the save button has been clicked.

- penColor (string; default 'black'):
    The pen color of the signature component.

- style (dict; optional):
    The style props of signature div."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'dash_sign'
    _type = 'DashSign'
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, penColor=Component.UNDEFINED, backgroundColor=Component.UNDEFINED, n_submit=Component.UNDEFINED, style=Component.UNDEFINED, data=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'backgroundColor', 'data', 'n_submit', 'penColor', 'style']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'backgroundColor', 'data', 'n_submit', 'penColor', 'style']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(DashSign, self).__init__(**args)
