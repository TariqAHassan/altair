# This file auto-generated by `generate_schema_interface.py`.
# Do not modify this file directly.

import traitlets as T
from ..baseobject import BaseObject
from .channeldefwithlegend import ChannelDefWithLegend
from .fielddef import FieldDef
from .orderchanneldef import OrderChannelDef
from .positionchanneldef import PositionChannelDef


class UnitEncoding(BaseObject):
    """Wrapper for Vega-Lite UnitEncoding definition.
    
    Attributes
    ----------
    color: ChannelDefWithLegend
        
    detail: Union(FieldDef, List(FieldDef))
        
    label: FieldDef
        
    opacity: ChannelDefWithLegend
        
    order: Union(OrderChannelDef, List(OrderChannelDef))
        
    path: Union(OrderChannelDef, List(OrderChannelDef))
        
    shape: ChannelDefWithLegend
        
    size: ChannelDefWithLegend
        
    text: FieldDef
        
    x: PositionChannelDef
        
    y: PositionChannelDef
        
    """
    color = T.Instance(ChannelDefWithLegend, allow_none=True, default_value=None)
    detail = T.Union([T.Instance(FieldDef, allow_none=True, default_value=None, help="""Interface for any kind of FieldDef;

For simplicity, we do not declare multiple interfaces of FieldDef like

we do for JSON schema."""), T.List(T.Instance(FieldDef, allow_none=True, default_value=None, help="""Interface for any kind of FieldDef;

For simplicity, we do not declare multiple interfaces of FieldDef like

we do for JSON schema."""), allow_none=True, default_value=None)])
    label = T.Instance(FieldDef, allow_none=True, default_value=None)
    opacity = T.Instance(ChannelDefWithLegend, allow_none=True, default_value=None)
    order = T.Union([T.Instance(OrderChannelDef, allow_none=True, default_value=None), T.List(T.Instance(OrderChannelDef, allow_none=True, default_value=None), allow_none=True, default_value=None)])
    path = T.Union([T.Instance(OrderChannelDef, allow_none=True, default_value=None), T.List(T.Instance(OrderChannelDef, allow_none=True, default_value=None), allow_none=True, default_value=None)])
    shape = T.Instance(ChannelDefWithLegend, allow_none=True, default_value=None)
    size = T.Instance(ChannelDefWithLegend, allow_none=True, default_value=None)
    text = T.Instance(FieldDef, allow_none=True, default_value=None)
    x = T.Instance(PositionChannelDef, allow_none=True, default_value=None)
    y = T.Instance(PositionChannelDef, allow_none=True, default_value=None)
    
    def __init__(self, color=None, detail=None, label=None, opacity=None, order=None, path=None, shape=None, size=None, text=None, x=None, y=None, **kwargs):
        kwds = dict(color=color, detail=detail, label=label, opacity=opacity, order=order, path=path, shape=shape, size=size, text=text, x=x, y=y)
        kwargs.update({k:v for k, v in kwds.items() if v is not None})
        super(UnitEncoding, self).__init__(**kwargs)