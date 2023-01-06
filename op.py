import bpy


def half(n):
    return n / 2


def pos_neg(n):
    calculated = {
        "pos": n,
        "neg": n * -1
    }
    return calculated


def foot(imperial_value):
    return imperial_value * 0.3048

# Run with:
# bpy.ops.object.generate_room()


def cube_ft(width=1, depth=1, height=1, x=0, y=0, z=0):
    # x, y, x are half
    bpy.ops.mesh.primitive_cube_add(
        size=foot(1), location=(foot(x), foot(y), foot(z)))
    bpy.context.object.scale = (1 * width, 1 * depth, 1 * height)


def generate_room(width=6, height=10, depth=6, wall_thickness=1, floor_thickness=1):
    # Width is equal too: |E| <-- x/2 --> |W|
    # Walls have origin center but to total width, height, depth we gave needs to be achieved, we need to offset the wall thickness by half via subtraction
    # The East and West wall will slot within the North and South walls
    # _____
    # -----
    # ||
    # ||
    # _____
    # -----
    #
    # East wall
    cube_ft(
        width=wall_thickness,
        height=height,
        depth=depth - (wall_thickness * 2),
        z=height / 2,
        x=half(pos_neg(width)["pos"]) - half(wall_thickness))
    # West wall
    cube_ft(
        width=wall_thickness,
        height=height,
        depth=depth - (wall_thickness * 2),
        z=height / 2,
        x=half(pos_neg(width)["neg"]) + half(wall_thickness))
    # North wall
    cube_ft(
        width=width,
        height=height,
        depth=wall_thickness,
        z=height / 2,
        y=half(pos_neg(depth)["pos"]) - half(wall_thickness)
    )
    # South wall
    cube_ft(
        width=width,
        height=height,
        depth=wall_thickness,
        z=height / 2,
        y=half(pos_neg(depth)["neg"]) + half(wall_thickness))
    # Floor
    cube_ft(
        width=width - wall_thickness * 2,
        height=floor_thickness - wall_thickness * 2,
        depth=depth - wall_thickness * 2,
        z=floor_thickness / 2,
        y=0
    )


class Generate_Room_Operator(bpy.types.Operator):
    bl_idname = "object.generate_room"
    bl_label = "generate_room"

    def execute(self, context):
        generate_room(
            width=30,
            depth=40,
            height=10,
            wall_thickness=.75
        )
        # cube_ft(width=6, height=6, depth=6)

        return {'FINISHED'}
