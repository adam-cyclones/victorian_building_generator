import bpy
from . import math_extra as math_extra


def cube_ft(parent, width=1, depth=1, height=1, x=0, y=0, z=0, name='cube_ft'):
    # x, y, x are math.half
    bpy.ops.mesh.primitive_cube_add(
        size=math_extra.foot(1),
        location=(math_extra.foot(x),
                  math_extra.foot(y),
                  math_extra.foot(z)),
    )
    bpy.context.active_object.name = name
    bpy.context.object.scale = (1 * width, 1 * depth, 1 * height)
    if parent:
        bpy.data.objects[name].parent = parent
